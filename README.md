# 🚗 Vehicle Tracker and Counter using YOLOv8 + Deep SORT

This project is a real-time vehicle tracking and counting system that detects and tracks vehicles crossing a defined line in traffic surveillance videos. It combines **YOLOv8** for object detection and **Deep SORT** for tracking, using OpenCV to visualize results dynamically.

## 🔧 Features

- Real-time object detection using **YOLOv8**
- Vehicle tracking with **Deep SORT**
- Counts vehicles as they cross a customizable virtual line
- Supports multiple video datasets
- Interactive interface to adjust the counting line with keyboard (`W`, `S`, `Q`)
- Only tracks specific vehicle classes (e.g., cars and trucks)

## 🧠 Tech Stack

- Python
- OpenCV
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- Deep SORT (via `deep_sort_realtime`)
- Numpy

## 📁 Dataset

Videos used for testing are stored in the `dataset/` directory. You can replace or add more surveillance footage to this folder.

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vehicle-tracker-yolo.git
   cd vehicle-tracker-yolo
   ```

2. Install dependencies

3. Run the main script:
   ```bash
   python vehicle_tracker.py
   ```

4. Use:
   - `W`: Move counting line up
   - `S`: Move counting line down
   - `Q`: Quit

## 📊 Output

The script displays the live video feed with:
- Bounding boxes for tracked vehicles
- Assigned tracking IDs
- A dynamic count of unique vehicles crossing the line
