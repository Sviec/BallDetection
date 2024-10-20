from scripts import train, tune, detect
from src.data import convert, load_data, prepare_directory
from config.paths import RELEVANT_DATA_PATH, DATA_PATH, VIDEO_PATH_1, OUTPUT_VIDEO_PATH


def main():
    load_data.load_data()
    prepare_directory.process_images(DATA_PATH, RELEVANT_DATA_PATH)
    convert.process_annotations_folder(DATA_PATH, RELEVANT_DATA_PATH)

    print('Tuning model...')
    tune.tune(epochs=5, iterations=10)
    print("Training model...")
    train.train(epochs=30, patience=10)

    detect.detect(VIDEO_PATH_1, OUTPUT_VIDEO_PATH)


if __name__ == "__main__":
    main()