import json
import os

def convert_coco_to_yolo(coco_json_path, output_dir, image_width, image_height):
    # Load COCO JSON file
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over each image in the dataset
    for image_data in coco_data['images']:
        image_id = image_data['id']
        image_name = image_data['file_name']
        keypoints_list = []

        # Find annotations for the current image
        for annotation in coco_data['annotations']:
            if annotation['image_id'] == image_id:
                keypoints = annotation['keypoints']
                keypoints_list.append(keypoints)

        # Skip images without annotations
        if not keypoints_list:
            continue

        # Create YOLO annotation file
        annotation_file_name = os.path.splitext(image_name)[0] + '.txt'
        annotation_file_path = os.path.join(output_dir, annotation_file_name)
        with open(annotation_file_path, 'w') as f:
            for keypoints in keypoints_list:
                # Find bounding box coordinates
                x_min = min(keypoints[0::3])
                y_min = min(keypoints[1::3])
                x_max = max(keypoints[0::3])
                y_max = max(keypoints[1::3])

                # Normalize bounding box coordinates to range [0, 1]
                x_center = (x_min + x_max) / (2 * image_width)
                y_center = (y_min + y_max) / (2 * image_height)
                width = (x_max - x_min) / image_width
                height = (y_max - y_min) / image_height

                # Write the annotation to the YOLO file
                f.write(f'{0} {round(x_center, 6)} {round(y_center, 6)} {round(width, 6)} {round(height, 6)} ')

                # Append normalized keypoints to the annotation
                for i in range(0, len(keypoints), 3):
                    x = round(keypoints[i] / image_width, 6)
                    y = round(keypoints[i + 1] / image_height, 6)
                    v = round(keypoints[i + 2], 6)
                    f.write(f'{x} {y} {v} ')
                f.write('\n')

    print('Conversion complete.')

# Example usage
coco_json_path = "C:\\PyCharm_project_final_year\\Yolov8_yoga_pose\\data_folder\\train_images\\vrkasanaa\\annotations\\person_keypoints_default.json"
output_dir = "C:\\PyCharm_project_final_year\\Yolov8_yoga_pose\\data_folder\\train\\label\\vrkasana"
image_width = 640 #Recommended for YOLOV8_Pose
image_height = 640 #Recommended for YOLOV8_Pose
print(output_dir)
convert_coco_to_yolo(coco_json_path, output_dir, image_width, image_height)