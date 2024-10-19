from SoccerNet.Downloader import SoccerNetDownloader


def load_data():
    mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="../data")
    mySoccerNetDownloader.downloadDataTask(task="gamestate-2024",
                                           split=["train", "valid", "test", "challenge"])