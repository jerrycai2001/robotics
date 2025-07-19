import cv2
from ultralytics import YOLO   # or your favourite detector
import numpy as np

# python - <<'PY'
import numpy, torch, cv2, ultralytics
print("NumPy :", numpy.__version__)
print("Torch  :", torch.__version__)
print("cv2    :", cv2.__version__)

# -------------
# Step 1.0 Validate camera streams properly
cap = cv2.VideoCapture(0)  # Try 1, 2, 3, etc. if 0 doesn't work

while True:
    ok, frame = cap.read()
    print("Frame status:", ok)
    if not ok:
        break
    cv2.imshow('Camera Test', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# # -------------
# # Step 1: Verify that OpenCV GUI works, even without a camera:


# img = np.zeros((480, 640, 3), dtype=np.uint8)
# cv2.imshow('Test Window', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # ----------------

# cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # HDMI capture card shows up as /dev/video0
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

# model = YOLO('yolov8n.pt')

# try:
#     while True:
#         ok, frame = cap.read()
#         if not ok:
#             print("No frame received. Check camera connection.")
#             break
#         res = model.track(frame, persist=True)
#         cv2.imshow('detections', res[0].plot())
#         if cv2.waitKey(1) & 0xFF == 27:   # ESC to quit
#             print("ESC pressed. Exiting.")
#             break
# except KeyboardInterrupt:
#     print("KeyboardInterrupt received. Exiting.")
# finally:
#     cap.release()
#     cv2.destroyAllWindows()
#     print("Resources released. Goodbye!")
