from scripts import train, tune
from src.data import convert, load_data, prepare_directory
from config.paths import RELEVANT_DATA_PATH, DATA_PATH


def main():
    # load_data.load_data()
    # prepare_directory.process_images(DATA_PATH, RELEVANT_DATA_PATH)
    # convert.process_annotations_folder(DATA_PATH, RELEVANT_DATA_PATH)

    # print('Tuning model...')
    # tune.tune(epochs=5, iterations=10)
    print("Training model...")
    train.train(epochs=30, patience=10)


if __name__ == "__main__":
    main()