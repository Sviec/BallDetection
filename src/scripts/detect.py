import os
from src.model.model import YOLOModel
from src.visualization.visualizer import visualize_detections
from src.utils.dataset import load_yaml_config
from config.paths import YAML_CONFIG_PATH, MODEL_PATH


def detect(video_path, output_video_path):
    # Путь к конфигурации
    config_path = YAML_CONFIG_PATH

    # Загружаем конфигурацию
    config = load_yaml_config(config_path)

    # Инициализируем модель
    yolo_model = YOLOModel(config)

    # Загружаем лучшие веса
    yolo_model.load_weights(MODEL_PATH)

    # Визуализация на видео
    visualize_detections(yolo_model, video_path, output_video_path)

