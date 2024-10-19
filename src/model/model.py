from ultralytics import YOLO
from config.paths import YAML_CONFIG_PATH


class YOLOModel:
    def __init__(self, config):
        self.config = config
        self.model = YOLO(f'{self.config["model"]["type"]}.pt')

    def train(self, epochs=30, patience=10):
        """
        Запуск обучения модели на основе параметров из конфигурации.
        """
        self.model.train(
            data=YAML_CONFIG_PATH,
            epochs=epochs,
            lr0=0.001,
            imgsz=self.config['model']['img_size'],
            batch=self.config['model']['batch'],
            workers=self.config['model']['workers'],
            single_cls=self.config['model']['single_cls'],
            verbose=self.config['model']['verbose'],
            fraction=self.config['model']['fraction'],
            plots=self.config['model']['plots'],
            patience=patience,
            project=self.config['output']['save_dir'],
            name='train_model',
        )

    def load_weights(self, weights_path):
        """
        Загружает предобученные веса модели.
        """
        self.model = YOLO(weights_path)

    def predict(self, input_data):
        """
        Запуск предсказаний модели.
        """
        return self.model(input_data)
