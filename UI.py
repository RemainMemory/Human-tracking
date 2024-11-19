# import tkinter as tk
# from tkinter import filedialog, messagebox
# from image_detection import detect_from_image
# from video_detection import detect_from_video
# from camera_detection import detect_from_camera
#
#
# class DetectionApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Real-Time Human Detection System")
#         self.root.geometry("600x450")
#         self.root.configure(bg="#2c3e50")  # 深色背景
#
#         # 创建标题
#         self.title_label = tk.Label(
#             root, text="Choose Detection Mode", font=("Arial", 24, "bold"),
#             fg="#ecf0f1", bg="#2c3e50"
#         )
#         self.title_label.pack(pady=30)
#
#         # 按钮容器
#         self.button_frame = tk.Frame(root, bg="#2c3e50")
#         self.button_frame.pack(pady=20)
#
#         # 图片检测按钮
#         self.image_button = self.create_button(
#             self.button_frame, "Detect from Image", self.open_image
#         )
#         self.image_button.grid(row=0, column=0, padx=10, pady=10)
#
#         # 视频检测按钮
#         self.video_button = self.create_button(
#             self.button_frame, "Detect from Video", self.open_video
#         )
#         self.video_button.grid(row=1, column=0, padx=10, pady=10)
#
#         # 摄像头检测按钮
#         self.camera_button = self.create_button(
#             self.button_frame, "Detect from Camera", self.detect_camera
#         )
#         self.camera_button.grid(row=2, column=0, padx=10, pady=10)
#
#         # 退出按钮
#         self.exit_button = self.create_button(
#             root, "Exit", self.root.quit
#         )
#         self.exit_button.pack(pady=30)
#
#     def create_button(self, parent, text, command):
#         """
#         创建带有悬停效果的按钮
#         """
#         button = tk.Button(
#             parent, text=text, font=("Arial", 16, "bold"),
#             command=command, width=25, height=2, bg="#ecf0f1", fg="#2c3e50",
#             relief="raised", bd=3, activebackground="#bdc3c7", activeforeground="#2c3e50"
#         )
#
#         # 悬停效果：改变背景和边框颜色
#         button.bind("<Enter>", lambda event, b=button: b.config(bg="#dcdcdc", bd=5))
#         button.bind("<Leave>", lambda event, b=button: b.config(bg="#ecf0f1", bd=3))
#
#         return button
#
#     def open_image(self):
#         file_path = filedialog.askopenfilename(
#             title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")]
#         )
#         if file_path:
#             detect_from_image(file_path)
#         else:
#             messagebox.showwarning("Warning", "No file selected.")
#
#     def open_video(self):
#         file_path = filedialog.askopenfilename(
#             title="Select Video", filetypes=[("Video files", "*.mp4 *.avi")]
#         )
#         if file_path:
#             detect_from_video(file_path)
#         else:
#             messagebox.showwarning("Warning", "No file selected.")
#
#     def detect_camera(self):
#         try:
#             detect_from_camera()
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to access camera: {e}")
#
#
# def run_ui():
#     root = tk.Tk()
#     app = DetectionApp(root)
#     root.mainloop()



import tkinter as tk
from tkinter import filedialog, messagebox
from image_detection import detect_from_image
from video_detection import VideoDetection
from camera_detection import detect_from_camera


class DetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Human Detection System")
        self.root.geometry("600x450")
        self.root.configure(bg="#34495e")  # 深色背景
        self.root.resizable(False, False)

        # 创建标题
        self.title_label = tk.Label(
            root, text="Choose Detection Mode", font=("Arial", 24, "bold"),
            fg="#ecf0f1", bg="#34495e"
        )
        self.title_label.pack(pady=30)

        # 按钮容器
        self.button_frame = tk.Frame(root, bg="#34495e")
        self.button_frame.pack(pady=20)

        # 图片检测按钮
        self.image_button = self.create_button(
            self.button_frame, "Detect from Image", self.open_image
        )
        self.image_button.grid(row=0, column=0, padx=10, pady=10)

        # 视频检测按钮
        self.video_button = self.create_button(
            self.button_frame, "Detect from Video", self.open_video
        )
        self.video_button.grid(row=1, column=0, padx=10, pady=10)

        # 摄像头检测按钮
        self.camera_button = self.create_button(
            self.button_frame, "Detect from Camera", self.detect_camera
        )
        self.camera_button.grid(row=2, column=0, padx=10, pady=10)

        # 退出按钮
        self.exit_button = self.create_button(
            root, "Exit", self.root.quit
        )
        self.exit_button.pack(pady=30)

    def create_button(self, parent, text, command):
        """
        创建带有悬停效果的按钮
        """
        button = tk.Button(
            parent, text=text, font=("Arial", 16, "bold"),
            command=command, width=25, height=2, bg="#ecf0f1", fg="#34495e",
            relief="raised", bd=3, activebackground="#bdc3c7", activeforeground="#34495e"
        )

        # 悬停效果：改变背景和边框颜色
        button.bind("<Enter>", lambda event, b=button: b.config(bg="#dcdcdc", bd=5))
        button.bind("<Leave>", lambda event, b=button: b.config(bg="#ecf0f1", bd=3))

        return button

    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            try:
                detect_from_image(file_path)
                messagebox.showinfo("Success", "Image Detection Completed!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to detect image: {e}")
        else:
            messagebox.showwarning("Warning", "No file selected.")

    def open_video(self):
        video_path = filedialog.askopenfilename(
            title="Select Video", filetypes=[("Video files", "*.mp4 *.avi")]
        )
        if video_path:
            try:
                video_detector = VideoDetection(threshold=0.7)
                results = video_detector.detect(video_path)
                video_detector.plot_results(results)
                video_detector.generate_report(results)
                messagebox.showinfo("Success", "Video Detection Completed and Report Generated!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to detect video: {e}")
        else:
            messagebox.showwarning("Warning", "No file selected.")

    def detect_camera(self):
        try:
            detect_from_camera()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to access camera: {e}")


def run_ui():
    root = tk.Tk()
    app = DetectionApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_ui()
