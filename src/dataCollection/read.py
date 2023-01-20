from Scraper import Scraper
from fileConstants import *


def read():
    folder = r"C:\Users\ydava\gestures\data\train"
    collection = NOISE_FILE_PREFIX
    collectionSize = 12
    pointCount = DATA_LENGTH

    scrape = Scraper(folder, collection, pointCount)

    try:
        scrape.writeMultiFile(collectionSize)
    except ValueError:
        print(f"Error Caugth: \n {ValueError}")


if __name__ == "__main__":
    read()