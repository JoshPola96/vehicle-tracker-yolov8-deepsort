# 🚗 Vehicle Tracker and Counter using YOLOv8 + Deep SORT

> **Scope** · Timeboxed technical assessment (short). Built to a brief under a fixed clock — scope decisions were deliberate.

> [!NOTE]
> **Built 2025. The ecosystem has moved since.**
> Dependencies here are unpinned, so a clean `pip install` today resolves to
> versions that did not exist when this was written and pandas 3.0, numpy 2.5 plus major releases of torch, ultralytics and transformers have all landed since. Expect install or
> runtime breakage on a fresh environment. What is on offer is the engineering
> approach and the decisions behind it, not a guaranteed-green build.
> Happy to bring it current if that would be useful — just ask.

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
