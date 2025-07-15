import cv2
from ultralytics import YOLO   # or your favourite detector

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # HDMI capture card shows up as /dev/video0
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

model = YOLO('yolov8n.pt')

while True:
    ok, frame = cap.read()
    if not ok:
        break
    res = model.track(frame, persist=True)
    cv2.imshow('detections', res[0].plot())
    if cv2.waitKey(1) & 0xFF == 27:   # ESC to quit
        break
cap.release()
cv2.destroyAllWindows()
