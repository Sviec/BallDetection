import os
import json
import shutil


def process_images(source_root, dest_root):
    """
    Проходит по каждой папке SNGS, переименовывает изображения на image_id согласно JSON аннотации
    и перемещает их в целевую папку.

    :param source_root: Путь к папке, содержащей папки train, test, valid, challenge.
    :param dest_root: Путь к целевой папке для изображений.
    """
    subdirs = ['train', 'test', 'valid']

    for subdir in subdirs:
        source_path = os.path.join(source_root, subdir)
        dest_images_path = os.path.join(dest_root, subdir, 'images')

        os.makedirs(dest_images_path, exist_ok=True)

        for folder in os.listdir(source_path):
            folder_path = os.path.join(source_path, folder)
            if os.path.isdir(folder_path):
                json_file_path = os.path.join(folder_path, 'Labels-GameState.json')
                img_folder = os.path.join(folder_path, 'img1')

                if os.path.exists(json_file_path) and os.path.exists(img_folder):
                    with open(json_file_path, 'r', encoding='utf-8') as json_file:
                        annotations = json.load(json_file)

                    for annotation in annotations['images']:
                        image_id = annotation['image_id']
                        file_name = annotation['file_name']

                        img_source_path = os.path.join(img_folder, file_name)
                        img_dest_name = f"{image_id}.jpg"
                        img_dest_path = os.path.join(dest_images_path, img_dest_name)

                        if os.path.exists(img_source_path):
                            shutil.copy2(img_source_path, img_dest_path)
                            print(f"Файл {file_name} переименован в {img_dest_name} и перемещен в {dest_images_path}")
                        else:
                            print(f"Файл {file_name} не найден в {img_folder}")


