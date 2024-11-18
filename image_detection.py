import cv2
from detection import DetectorAPI


def detect_from_image(image_path):
    detector = DetectorAPI()
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not open or find the image.")
        return

    boxes, _, _, _ = detector.process_frame(image)
    for box in boxes:
        cv2.rectangle(image, (box[1], box[0]), (box[3], box[2]), (0, 255, 0), 2)
    cv2.imshow("Image Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
