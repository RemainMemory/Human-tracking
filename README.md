# Real-Time Human Detection System

## **项目简介**
本项目是一个基于 **TensorFlow** 和 **OpenCV** 的实时人体检测系统。通过加载预训练的模型文件（`frozen_inference_graph.pb`），实现从图片、视频和摄像头输入中检测人员。项目支持多种检测模式，用户可以选择图片、视频文件或实时摄像头输入进行检测。

---

## **功能特性**
- **图片检测**：从图片文件中检测人员。
- **视频检测**：从视频文件中逐帧检测人员。
- **摄像头检测**：通过电脑摄像头实时检测人员。
- **用户友好界面**：使用 `Tkinter` 提供简单直观的操作界面。

---

## **安装要求**

### **系统要求**
- **操作系统**：Windows 或 Linux
- **Python 版本**：3.10
- **依赖**：
  - TensorFlow
  - OpenCV
  - NumPy
  - Matplotlib
  - FPDF
  - Python-dotenv

---

## **环境配置**

### **通用步骤（Windows 和 Linux）**
1. **克隆项目**
   使用以下命令克隆项目：
   ```bash
   git clone https://github.com/RemainMemory/Human-tracking.git
   cd Human-tracking
   ```

2. **创建 Conda 环境**
   在项目根目录中，基于 `environment.yml` 文件创建 Conda 环境：
   ```bash
   conda env create --prefix ./env -f environment.yml
   ```

3. **激活环境**
   激活 Conda 环境：
   ```bash
   conda activate ./env
   ```

4. **运行项目**
   确保环境激活后运行程序：
   ```bash
   python main.py
   ```

5. **退出环境**
   完成工作后，退出环境：
   ```bash
   conda deactivate
   ```

---

## **目录结构**
```
├── main.py                # 程序入口文件
├── UI.py                  # 用户界面模块
├── detection.py           # 检测逻辑模块
├── image_detection.py     # 图片检测逻辑
├── video_detection.py     # 视频检测逻辑
├── camera_detection.py    # 实时摄像头检测逻辑
├── environment.yml        # 环境配置文件
├── frozen_inference_graph.pb  # 预训练模型文件（需单独下载）
└── README.md              # 项目说明文件
```

---

## **使用说明**

### **启动项目**
1. 启动程序后，界面提供以下选项：
   - `Detect from Image`：选择图片文件进行检测。
   - `Detect from Video`：选择视频文件进行检测。
   - `Detect from Camera`：通过摄像头实时检测人员。
   - `Exit`：退出程序。

2. **选择检测模式**：
   - 图片和视频检测会弹出文件选择器，选择所需文件后自动开始检测。
   - 摄像头检测将实时显示检测结果，按 `q` 键或点击 `Exit` 按钮退出。

---

## **常见问题**

### **1. 无法加载 TensorFlow 模型**
- 确保 `frozen_inference_graph.pb` 文件已下载并放置在项目根目录。
- 模型文件可从 [TensorFlow Model Zoo](https://github.com/tensorflow/models) 获取。

### **2. 摄像头无法正常工作**
- 检查系统权限，确保 Python 有权访问摄像头。
- 在 Linux 系统中，运行以下命令查看摄像头设备是否可用：
  ```bash
  ls /dev/video*
  ```

### **3. 缺少依赖**
- 如果运行时提示某些模块未安装，可以手动安装：
  ```bash
  pip install <missing-package>
  ```
  之后更新 `environment.yml` 文件：
  ```bash
  conda env export --prefix ./env > environment.yml
  ```

---

## **技术栈**
- **语言**：Python
- **框架**：TensorFlow, OpenCV, Tkinter
- **工具**：NumPy, Matplotlib, FPDF, Python-dotenv

---

## **贡献**
欢迎任何贡献或改进建议！请提交 Pull Request 或在 Issue 区域提出问题。

---

## **许可证**
本项目基于 MIT 许可证开源。