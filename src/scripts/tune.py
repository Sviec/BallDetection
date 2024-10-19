from src.model.model import YOLOModel
from src.utils.dataset import load_yaml_config
from config.paths import YAML_CONFIG_PATH


def tune(epochs, iterations):
    # Путь к конфигурации
    config_path = YAML_CONFIG_PATH

    # Загружаем конфигурацию
    config = load_yaml_config(config_path)

    # Инициализируем модель
    yolo_model = YOLOModel(config)

    # Запуск оптимизации гиперпараметров
    yolo_model.model.tune(
        data=YAML_CONFIG_PATH,
        epochs=epochs,
        iterations=iterations,
        imgsz=config['model']['img_size'],
        fraction=config['model']['fraction'],
        optimizer='AdamW',
    )
