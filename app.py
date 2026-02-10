import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np

# Configuration Objects

BaseOptions = python.BaseOptions
HandLandmarker= vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
visionRunningMode = vision.RunningMode

# Model File path
model_path = "hand_landmarker.task"

# Options configuration
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=visionRunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
)
# Creating the detector object
landmarker = HandLandmarker.create_from_options(options)

# hand Landmark conncetions for drawing
# Hand landmark connections for drawing
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),  # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),  # Index
    (5, 9), (9, 10), (10, 11), (11, 12),  # Middle
    (9, 13), (13, 14), (14, 15), (15, 16),  # Ring
    (13, 17), (17, 18), (18, 19), (19, 20),  # Pinky
    (0, 17)  # Palm
]

# Drawing function
def draw_landmarks_on_image(image, detection_result):
    """Draws the hand landmarks and connections on the image."""
    if not detection_result.hand_landmarks:
        return image

    annotated_image = image.copy()
    height, width, _ = annotated_image.shape

    for hand_landmarks in detection_result.hand_landmarks:
        # Draw landmarks
        for landmark in hand_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            cv2.circle(annotated_image, (x, y), 5, (0, 255, 0), -1)
        # Draw connections
        for connection in HAND_CONNECTIONS:
            start_idx, end_idx = connection
            start_landmark = hand_landmarks[start_idx]
            end_landmark = hand_landmarks[end_idx]
            start_point = (int(start_landmark.x * width), int(start_landmark.y * height))
            end_point = (int(end_landmark.x * width), int(end_landmark.y * height))
            cv2.line(annotated_image, start_point, end_point, (0, 255, 0), 2)

    return annotated_image

# Video Capture and Processing
cap = cv2.VideoCapture(0)
# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')   # or 'MJPG', 'MP4V'
out = cv2.VideoWriter('Data Sources and Artifacts/output.avi', fourcc, 20.0, (640,480))
frame_count=0
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
       # Save the frame to output file

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # ✓ Create MediaPipe Image object
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    
    # Detect hands with timestamp
    frame_timestamp_ms = frame_count * 33  # Approximate timestamp (33ms per frame for ~30fps)
    detection_result = landmarker.detect_for_video(mp_image, frame_timestamp_ms)
    # Perform hand landmark detection
    frame_count += 1

    # Draw landmarks on the original frame
    annotated_frame = draw_landmarks_on_image(frame, detection_result)

    # Display the annotated frame
    cv2.imshow('Hand Landmarker', annotated_frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break
    # Write the frame to output file
    out.write(annotated_frame)
    frame_count += 1

#Cleanup
cap.release()
cv2.destroyAllWindows()
out.release()
landmarker.close()
print("Hand tracking closed")

    