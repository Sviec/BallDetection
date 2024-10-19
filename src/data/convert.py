import json
import os


def convert_annotation_to_yolo(json_path, output_dir):
    """
    Конвертирует аннотацию из формата JSON в формат YOLO.

    :param json_path: Путь к файлу аннотации в формате JSON.
    :param output_dir: Путь к директории, где будут сохранены выходные файлы аннотаций.
    """
    os.makedirs(f'{output_dir}/labels', exist_ok=True)
    with open(json_path, 'r') as f:
        data = json.load(f)

    for image in data['images']:
        image_id = image['image_id']
        width = image['width']
        height = image['height']

        annotation_file_path = os.path.join(f"{output_dir}/labels", f"{image_id}.txt")

        with open(annotation_file_path, 'w') as annotation_file:
            for annotation in data['annotations']:
                if annotation['image_id'] == image_id and annotation['category_id'] == 4:
                    # Получение bbox
                    x = annotation['bbox_image']['x_center'] / width
                    y = annotation['bbox_image']['y_center'] / height
                    w = annotation['bbox_image']['w'] / width
                    h = annotation['bbox_image']['h'] / height

                    annotation_file.write(f"0 {x} {y} {w} {h}\n")
        print(f'Access convert for file {annotation_file_path}')


def process_annotations_folder(annotations_folder, output_dir):
    """
    Обрабатывает все файлы аннотаций в указанной папке.

    :param annotations_folder: Путь к папке с аннотациями в формате JSON.
    :param output_dir: Путь к директории, где будут сохранены выходные файлы аннотаций.
    """
    for data_dir in os.listdir(annotations_folder):
        if data_dir in ['test', 'train', 'valid']:
            walk_file(f"{annotations_folder}/{data_dir}", os.path.join(output_dir, data_dir))


def walk_file(path, output_path):
    for i in os.listdir(path):
        if os.path.isdir(f'{path}/{i}'):
            print(f'Переходим в папку: {i}')
            walk_file(f'{path}/{i}', output_path)
        elif i.endswith('.json') and i.startswith('Labels'):
            json_path = os.path.join(path, i)
            convert_annotation_to_yolo(json_path, output_path)

