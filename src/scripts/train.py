from src.model.model import YOLOModel
from src.utils.dataset import load_yaml_config
from config.paths import YAML_CONFIG_PATH


def train(epochs, patience):
    # Путь к конфигурации
    config_path = YAML_CONFIG_PATH

    # Загружаем конфигурацию
    config = load_yaml_config(config_path)

    # Инициализируем и обучаем модель
    yolo_model = YOLOModel(config)
    yolo_model.train(epochs, patience)
