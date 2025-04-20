import cv2
import numpy as np
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import random

# Function to assign colors to tracked objects
def getColours(cls_num):
    random.seed(cls_num)
    return tuple(random.randint(0, 255) for _ in range(3))

model = YOLO('yolov8n.pt')  

tracker = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)

video_list=[
    'dataset/rene_video.mov',
    'dataset/rouen_video.avi',
    'dataset/sherbrooke_video.avi',
    'dataset/stmarc_video.avi'
]

video_path = random.choice(video_list)
cap = cv2.VideoCapture(video_path)

# Get frame dimensions
ret, frame = cap.read()
if not ret:
    print("Error: Unable to read video.")
    cap.release()
    exit()

frame_height, frame_width = frame.shape[:2]

# Define counting line in center of frame
counting_line_y = frame_height // 2
counted_vehicles = set()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame for better accuracy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    frame = cv2.cvtColor(gray, cv2.COLOR_YUV2BGR)
    
    # Run YOLO detection
    results = model.track(frame, persist=True)  

    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            class_id = int(box.cls[0].item())

            if class_id == 2:  # Only track cars, trucks - 7
                detections.append(([x1, y1, x2, y2], conf, class_id))

    # Run DeepSORT tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    # Draw tracking results
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb()
        x1, y1, x2, y2 = map(int, ltrb)

        color = getColours(track_id)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f'ID: {track_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Check if vehicle crosses the counting line
        center_y = (y1 + y2) // 2  # Get Y position of vehicle center
        if track_id not in counted_vehicles and center_y >= counting_line_y:
            counted_vehicles.add(track_id)  # Mark vehicle as counted

    # Draw counting line
    cv2.line(frame, (50, counting_line_y), (frame_width - 50, counting_line_y), (0, 255, 255), 2)
    cv2.putText(frame, f'Count: {len(counted_vehicles)}', (50, counting_line_y - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Show video frame
    cv2.imshow("Vehicle Tracking & Counting", frame)

    # Live adjust the counting line
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break  # Quit
    elif key == ord('w'):
        counting_line_y = max(50, counting_line_y - 5)  # Move line up
    elif key == ord('s'):
        counting_line_y = min(frame.shape[0] - 50, counting_line_y + 5)  # Move line down

# Release resources
cap.release()
cv2.destroyAllWindows()
