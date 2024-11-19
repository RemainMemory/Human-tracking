# import cv2
# from detection import DetectorAPI
#
#
# def detect_from_video(video_path):
#     detector = DetectorAPI()
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Could not open video.")
#         return
#
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         boxes, _, _, _ = detector.process_frame(frame)
#         for box in boxes:
#             cv2.rectangle(frame, (box[1], box[0]), (box[3], box[2]), (0, 255, 0), 2)
#         cv2.imshow("Video Detection", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()


import cv2
import matplotlib.pyplot as plt
from fpdf import FPDF
from detection import DetectorAPI


class VideoDetection:
    def __init__(self, threshold=0.7):
        """
        Initialize VideoDetection with a given confidence threshold.

        Args:
            threshold (float): Confidence threshold for detection.
        """
        self.threshold = threshold
        self.detector = DetectorAPI()

    def detect(self, video_path):
        """
        Detect humans in a video file.

        Args:
            video_path (str): Path to the video file.

        Returns:
            dict: Results including frame counts, human counts, and accuracy stats.
        """
        cap = cv2.VideoCapture(video_path)
        max_count = 0
        framex = []
        county = []
        max_list = []
        avg_acc_list = []
        max_avg_acc_list = []
        max_acc = 0
        max_avg_acc = 0
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (800, 600))
            boxes, scores, classes, num = self.detector.process_frame(frame)
            person = 0
            acc = 0

            for i in range(len(boxes)):
                if classes[i] == 1 and scores[i] > self.threshold:
                    box = boxes[i]
                    person += 1
                    cv2.rectangle(frame, (box[1], box[0]), (box[3], box[2]), (255, 0, 0), 2)
                    acc += scores[i]
                    if scores[i] > max_acc:
                        max_acc = scores[i]

            if person > max_count:
                max_count = person

            frame_count += 1
            framex.append(frame_count)
            county.append(person)
            max_list.append(max_count)

            if person >= 1:
                avg_acc = acc / person
                avg_acc_list.append(avg_acc)
                if avg_acc > max_avg_acc:
                    max_avg_acc = avg_acc
            else:
                avg_acc_list.append(0)

            max_avg_acc_list.append(max_avg_acc)

            cv2.imshow("Human Detection from Video", frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        return {
            "framex": framex,
            "county": county,
            "max_list": max_list,
            "avg_acc_list": avg_acc_list,
            "max_avg_acc_list": max_avg_acc_list,
            "max_count": max_count,
            "max_acc": max_acc,
            "max_avg_acc": max_avg_acc,
        }

    def plot_results(self, results):
        """
        Plot detection results (human count and accuracy).

        Args:
            results (dict): Detection results returned by detect().
        """
        framex = results["framex"]
        county = results["county"]
        max_list = results["max_list"]
        avg_acc_list = results["avg_acc_list"]
        max_avg_acc_list = results["max_avg_acc_list"]

        # Enumeration Plot
        plt.figure(facecolor='orange')
        ax = plt.axes()
        ax.set_facecolor("yellow")
        plt.plot(framex, county, label="Human Count", color="green", marker='o', markerfacecolor='blue')
        plt.plot(framex, max_list, label="Max. Human Count", linestyle='dashed', color='fuchsia')
        plt.xlabel('Frame')
        plt.ylabel('Human Count')
        plt.legend()
        plt.title("Enumeration Plot")
        plt.show()

        # Accuracy Plot
        plt.figure(facecolor='orange')
        ax = plt.axes()
        ax.set_facecolor("yellow")
        plt.plot(framex, avg_acc_list, label="Avg. Accuracy", color="green", marker='o', markerfacecolor='blue')
        plt.plot(framex, max_avg_acc_list, label="Max. Avg. Accuracy", linestyle='dashed', color='fuchsia')
        plt.xlabel('Frame')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.title("Accuracy Plot")
        plt.show()

    def generate_report(self, results, output_path='Crowd_Report.pdf'):
        """
        Generate a PDF report of the detection results.

        Args:
            results (dict): Detection results returned by detect().
            output_path (str): File path to save the report.
        """
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", "", 20)
        pdf.set_text_color(128, 0, 0)

        max_count = results["max_count"]
        max_acc = results["max_acc"]
        max_avg_acc = results["max_avg_acc"]

        pdf.text(125, 150, str(max_count))
        pdf.text(105, 163, str(max_acc))
        pdf.text(125, 175, str(max_avg_acc))

        if max_count > 25:
            pdf.text(26, 220, "Max. Human Detected is greater than MAX LIMIT.")
            pdf.text(70, 235, "Region is Crowded.")
        else:
            pdf.text(26, 220, "Max. Human Detected is in range of MAX LIMIT.")
            pdf.text(65, 235, "Region is not Crowded.")

        pdf.output(output_path)
