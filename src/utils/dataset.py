import yaml


def load_yaml_config(config_path):
    """
    Загружает конфигурационный файл в формате YAML.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
