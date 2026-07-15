import cv2
from ultralytics import YOLO

video_name = "30sec.mp4"


model = YOLO(r"advance_tasks\Yolo_task\runs\detect\train\weights\best.pt")

cap = cv2.VideoCapture(rf"advance_tasks\Yolo_task\videos_infer\{video_name}")

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter(rf"advance_tasks\Yolo_task\output\detected_{video_name}",
                         cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
while True:
    ok, frame = cap.read()
    if not ok:
        break

    results = model(frame, conf=0.48)

    frame_box = results[0].plot()

    out.write(frame_box)

cap.release()
out.release()