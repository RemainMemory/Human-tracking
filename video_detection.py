import cv2
from detection import DetectorAPI


def detect_from_video(video_path):
    detector = DetectorAPI()
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        boxes, _, _, _ = detector.process_frame(frame)
        for box in boxes:
            cv2.rectangle(frame, (box[1], box[0]), (box[3], box[2]), (0, 255, 0), 2)
        cv2.imshow("Video Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
