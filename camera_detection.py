import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox as mbox
from fpdf import FPDF
from detection import DetectorAPI


def detect_from_camera():
    max_count3 = 0
    framex3 = []
    county3 = []
    max3 = []
    avg_acc3_list = []
    max_avg_acc3_list = []
    max_acc3 = 0
    max_avg_acc3 = 0

    # 初始化摄像头
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Error: Could not access the camera.")
        return

    odapi = DetectorAPI()
    threshold = 0.7  # 置信度阈值

    while True:
        check, frame = video.read()
        if not check:
            break

        img = cv2.resize(frame, (800, 600))
        boxes, scores, classes, num = odapi.process_frame(img)
        person_count = 0
        acc = 0

        for i in range(len(boxes)):
            # 只检测类别为 "person" 且置信度高于阈值的物体
            if classes[i] == 1 and scores[i] > threshold:
                box = boxes[i]
                person_count += 1
                cv2.rectangle(img, (box[1], box[0]), (box[3], box[2]), (0, 255, 0), 2)
                cv2.putText(img, f'Person {person_count} ({scores[i]:.2f})',
                            (box[1], box[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                acc += scores[i]

        # 更新最大计数
        max_count3 = max(max_count3, person_count)
        county3.append(person_count)

        cv2.imshow("Real-Time Human Detection", img)

        # 退出检测按键
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头资源
    video.release()
    cv2.destroyAllWindows()

    # 生成报告
    generate_report(max_count3, max_acc3, max_avg_acc3)
    print("Detection completed and report generated.")


def generate_report(max_count, max_acc, max_avg_acc):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", "", 20)
    pdf.set_text_color(128, 0, 0)
    pdf.text(10, 30, f"Max Count: {max_count}")
    pdf.text(10, 40, f"Max Accuracy: {max_acc:.2f}")
    pdf.text(10, 50, f"Max Avg Accuracy: {max_avg_acc:.2f}")

    if max_count > 25:
        pdf.text(10, 70, "Crowded Region Detected.")
    else:
        pdf.text(10, 70, "Crowd Level is Acceptable.")

    pdf.output('Crowd_Report.pdf')
    mbox.showinfo("Status", "Report Generated Successfully")
