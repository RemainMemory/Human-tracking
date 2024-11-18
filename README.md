## **README.md**

# Real-Time Human Detection System

## **项目简介**
本项目是一个基于 **TensorFlow** 和 **OpenCV** 的实时人体检测系统。它通过加载预训练的模型文件（`frozen_inference_graph.pb`），实现从图片、视频和摄像头输入中检测人员。此项目支持多种检测模式，用户可以选择图片、视频文件或实时摄像头输入进行检测。

## **功能特性**
- **图片检测**：从图片文件中检测人员。
- **视频检测**：从视频文件中逐帧检测人员。
- **摄像头检测**：通过电脑摄像头实时检测人员。
- **用户友好界面**：使用 `Tkinter` 实现简单直观的界面。

---

## **目录结构**
```
├── main.py                # 程序入口文件
├── UI.py                  # 用户界面模块
├── detection.py           # 检测逻辑模块
├── image_detection.py     # 图片检测逻辑
├── video_detection.py     # 视频检测逻辑
├── camera_detection.py    # 实时摄像头检测逻辑
├── requirements.txt       # 依赖库列表
└── frozen_inference_graph.pb  # 预训练模型（需手动下载）
```

---

## **安装要求**

### **系统要求**
- Python 3.8 或以上版本
- TensorFlow 2.x
- OpenCV
- NumPy
- Matplotlib

### **依赖安装**
1. **克隆项目**
   ```bash
   git clone https://github.com/your-repo/real-time-human-detection.git
   cd real-time-human-detection
   ```

2. **创建并激活虚拟环境**
   ```bash
   python -m venv HumanDetectEnv
   source HumanDetectEnv/bin/activate  # macOS / Linux
   HumanDetectEnv\Scripts\activate     # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **下载预训练模型**
   - 请确保 `frozen_inference_graph.pb` 文件已下载并放置在项目根目录中。可以从 [TensorFlow Model Zoo](https://github.com/tensorflow/models) 获取。

---

## **使用说明**

### **运行项目**
在项目根目录下，执行以下命令启动程序：
```bash
python main.py
```

### **操作步骤**
1. **启动程序后**，会出现一个用户界面，提供以下选项：
   - `Detect from Image`：选择图片文件进行检测。
   - `Detect from Video`：选择视频文件进行检测。
   - `Detect from Camera`：通过摄像头实时检测。
   - `Exit`：退出程序。

2. **选择检测模式**：
   - 图片和视频检测将弹出文件选择器，选择所需文件后自动开始检测。
   - 摄像头检测将实时显示检测结果，按 `q` 键或点击 `Exit` 按钮退出。

---

## **文件说明**

### **1. main.py**
程序的入口文件，负责启动用户界面。

### **2. UI.py**
使用 `Tkinter` 创建用户界面，提供检测模式选择和退出功能。

### **3. detection.py**
封装了 TensorFlow 模型的加载和推理逻辑，主要包括：
- **DetectorAPI** 类：用于加载冻结模型并执行物体检测。
- `process_frame()` 方法：对输入的图像进行检测并返回检测结果。

### **4. image_detection.py**
从图片文件中检测人员，并在图片上绘制检测框。

### **5. video_detection.py**
从视频文件中逐帧检测人员，并在视频帧上绘制检测框。

### **6. camera_detection.py**
使用电脑摄像头进行实时检测，并在检测到的人员上绘制检测框。

---

## **常见问题**

1. **无法加载 TensorFlow 模型**
   - 确保 `frozen_inference_graph.pb` 文件已正确下载，并放置在项目根目录中。

2. **摄像头无法正常工作**
   - 检查系统权限，确保 Python 有权访问摄像头。
   - 如果使用 macOS，可能需要在系统设置中手动授予权限。

3. **依赖安装问题**
   - 请确保使用 Python 3.8 及以上版本，并安装了正确的 TensorFlow 版本。
   - 使用 `pip install -r requirements.txt` 确保所有依赖正确安装。

---

## **技术栈**
- **语言**：Python
- **框架**：TensorFlow, OpenCV, Tkinter
- **工具**：NumPy, Matplotlib

---

## **贡献**
欢迎任何贡献或改进建议！请提交 Pull Request 或在 Issue 区域提出问题。

---

## **许可证**
本项目基于 MIT 许可证开源。
