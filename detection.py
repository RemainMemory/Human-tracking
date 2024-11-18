import numpy as np
import tensorflow.compat.v1 as tf

# 禁用 TensorFlow 2.x 的行为，启用 TensorFlow 1.x 的兼容模式
tf.disable_v2_behavior()


class DetectorAPI:
    def __init__(self, model_path='frozen_inference_graph.pb', threshold=0.7):
        """
        初始化检测器类，加载预训练的 TensorFlow 模型。

        参数：
        - model_path: 冻结模型的路径
        - threshold: 检测的置信度阈值，低于该值的检测结果将被过滤掉
        """
        self.model_path = model_path
        self.threshold = threshold
        self.load_model()

    def load_model(self):
        """
        加载冻结的 TensorFlow 模型。
        """
        try:
            self.detection_graph = tf.Graph()
            with self.detection_graph.as_default():
                od_graph_def = tf.GraphDef()
                # 加载冻结的推理图
                with tf.gfile.GFile(self.model_path, 'rb') as fid:
                    serialized_graph = fid.read()
                    od_graph_def.ParseFromString(serialized_graph)
                    tf.import_graph_def(od_graph_def, name='')

            # 创建会话
            self.sess = tf.Session(graph=self.detection_graph)

            # 获取输入和输出张量的引用
            self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
            self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
            self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
            self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
            self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
            print("Model loaded successfully.")

        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    def process_frame(self, image):
        """
        处理输入图像并返回检测结果。

        参数：
        - image: 输入的图像 (numpy 数组)

        返回：
        - boxes_list: 检测框的坐标列表
        - scores: 检测到的物体置信度得分列表
        - classes: 检测到的物体类别列表
        - num: 检测到的物体数量
        """
        try:
            # 扩展图像维度以符合模型输入要求
            image_np_expanded = np.expand_dims(image, axis=0)

            # 运行推理
            (boxes, scores, classes, num) = self.sess.run(
                [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
                feed_dict={self.image_tensor: image_np_expanded}
            )

            # 获取图像高度和宽度
            im_height, im_width, _ = image.shape

            # 转换检测框的坐标并过滤置信度低于阈值的结果
            boxes_list = [
                (int(boxes[0, i, 0] * im_height), int(boxes[0, i, 1] * im_width),
                 int(boxes[0, i, 2] * im_height), int(boxes[0, i, 3] * im_width))
                for i in range(int(num[0])) if scores[0, i] > self.threshold
            ]

            return boxes_list, scores[0].tolist(), [int(x) for x in classes[0].tolist()], int(num[0])

        except Exception as e:
            print(f"Error processing frame: {e}")
            return [], [], [], 0

    def close(self):
        """
        关闭 TensorFlow 会话，释放资源。
        """
        self.sess.close()
        print("Session closed successfully.")
