# Yolov8_yoga_pose


About Dataset:
The dataset created for this project follows a systematic approach to collect and annotate yoga pose images for training and validation purposes. Here's a brief description of the dataset creation process:
1. Data Collection: A total of 500-600 images were collected specifically for yoga poses. Each yoga pose category was represented by around 100 images, ensuring diversity and coverage of various poses.
2. Data Split: The collected images were divided into two parts: training images and validation images. This division helps in training the model on one set of data and evaluating its performance on another set to measure generalization.
3. Annotation Tool: The annotation process was carried out using the CVAT.ai platform, which provides tools for annotating keypoints in images. Key keypoints relevant to yoga poses were annotated on the images to create a detailed pose description.
4. Skeleton Creation: A 5-skeleton structure was defined for annotating key body joints and landmarks necessary for identifying yoga postures accurately. This skeleton structure likely included keypoints for major joints like shoulders, elbows, wrists, hips, and knees, depending on the yoga poses being annotated.
5. Annotation Application: Annotations created using CVAT.ai were then applied to the training and validation images based on the defined skeleton. This step ensures that each image has corresponding keypoint annotations for the yoga poses depicted.
6. Export Format: The annotated data was exported in the COCO Keypoint 1.0 format, a widely used format for keypoint annotations in computer vision tasks. The exported data was packaged into zip files for further processing.
7. Data Conversion: To make the dataset compatible with the YOLOv8 model, a custom function was developed to convert the COCO keypoint files (in JSON format) into YOLO format text files. This conversion process mapped the keypoint annotations to bounding boxes, which are essential for YOLO-based object detection models.
8. Final Dataset: After completing the conversion and formatting steps, the dataset was ready for training the YOLOv8 model for yoga posture detection and correction tasks. The dataset includes both training and validation images along with their corresponding annotations in the YOLO format.
This meticulously created dataset forms the foundation for training the machine learning model to accurately detect and correct yoga postures based on keypoint annotations. It reflects a structured approach to data collection and annotation essential for developing robust computer vision applications in the yoga domain.
The below images are belonging to the five different classes viz, gingivitis, Caries, Ulcer, Tooth discoloration.

Requirement:
Python:
Python is a high-level programming language known for its simplicity, readability, and vast ecosystem of libraries and frameworks. In the context of the project "Yoga Posture Detection and Correction Using YOLOv8 with Keypoints," Python serves as the primary programming language for developing the computer vision algorithms, data processing, user interface, and system integration.
Python offers a wide range of libraries and tools for machine learning, computer vision, and web development, making it suitable for implementing complex projects like posture detection and correction.
Popular libraries such as NumPy, OpenCV, TensorFlow, and PyTorch are commonly used in Python for deep learning, image processing, and neural network modeling, which are essential components of this project.
PyCharm (in conda environment):
PyCharm is an integrated development environment (IDE) specifically designed for Python development. It provides features such as code completion, debugging tools, version control integration, and project management functionalities.
Conda Environment:
  - Conda is a package and environment management system for installing and managing software packages and dependencies. Using PyCharm within a Conda environment ensures that the project's specific dependencies and versions are isolated and managed efficiently.
  - Conda environments allow for creating a reproducible and consistent development environment across different machines and platforms, enhancing project collaboration and deployment.
Ultralytics:
Ultralytics is a deep learning research group known for developing and maintaining state-of-the-art object detection models, including YOLOv5 and YOLOv8. In the context of this project, the Ultralytics library provides implementations of YOLOv8 and related utilities for object detection tasks.
YOLOv8 Implementation:
The Ultralytics library simplifies the implementation of YOLOv8 for object detection tasks, offering functionalities for model training, inference, evaluation, and visualization.
Leveraging the Ultralytics library ensures access to optimized and up-to-date implementations of YOLOv8, saving time and effort in model development and experimentation.
Streamlit: 
Streamlit is a popular open-source framework for building interactive web systems  specifically designed for data science and machine learning.
? Interactive data visualization: Data visualization is a fundamental aspect of data  science, and Streamlit excels in this area. 
? Integration with machine learning libraries: Streamlit seamlessly integrates  with popular machine learning libraries, such as TensorFlow, PyTorch, and scikit learn. This allows data scientists to build end-to-end machine learning pipelines  within Streamlit systems.
 Performance Analysis:

Flow of Yoga Posture Detection and Correction System:

![image](https://github.com/Prathamesh9764/Yolov8_yoga_pose/assets/92622855/0862488e-d6e7-474d-8985-86af2edde50d)








Interface:

![image](https://github.com/Prathamesh9764/Yolov8_yoga_pose/assets/92622855/be3637ff-f49d-4aad-82fa-bb0d7ccd50a9)


URL : https://yoga-posture-detection-and-correction-using-yolov8.streamlit.app/


