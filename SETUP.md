# Hand Tracking Setup Guide

## Current Status
✓ Dependencies installed  
✓ app.py rewritten to use MediaPipe Tasks API  
✓ numpy/h5py compatibility fixed  
⏳ **Need: hand_landmarker.task model file**

## Getting the Model File

You need to download the `hand_landmarker.task` model (~47 MB) from one of these sources:

### Option 1: MediaPipe Solutions Hub (Recommended)
1. Visit: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker
2. Scroll down to "Download a model"
3. Download `hand_landmarker.task`
4. Place it in: `C:\Users\ssubh\Hand-Tracking-Using-Opencv\hand_landmarker.task`

### Option 2: GitHub (Mirror)
```powershell
cd C:\Users\ssubh\Hand-Tracking-Using-Opencv
Invoke-WebRequest -Uri "https://github.com/google/mediapipe/raw/master/mediapipe/tasks/cc/vision/hand_landmarker/models/hand_landmarker.task" -OutFile "hand_landmarker.task"
```

### Option 3: Automated Download
```powershell
cd C:\Users\ssubh\Hand-Tracking-Using-Opencv
handenv\Scripts\python.exe download_model.py
```

## Running the App

Once the model file is in place:

```powershell
cd C:\Users\ssubh\Hand-Tracking-Using-Opencv
handenv\Scripts\python.exe app.py
```

Press **Q** to quit the application.

## Troubleshooting

If you get errors about missing `hand_landmarker.task`:
- Ensure the file is in the root of this folder
- Check file size is ~47 MB (not a 404 error page)
- Verify filename is exactly `hand_landmarker.task` (case-sensitive on Linux)

## What's New
- Changed from deprecated `mp.solutions.hands` API (mediapipe ≤0.8)
- Now uses modern `HandLandmarker` from `mediapipe.tasks` (0.10+)
- Detects up to 2 hands simultaneously
- Real-time FPS display
