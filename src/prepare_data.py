import os
import shutil

import urllib.request
from loguru import logger


def download_file(directory, filename):
    url = f"https://github.com/khanhnamle1994/instacart-orders/raw/master/data/{filename}?download="
    logger.debug(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, os.path.join(directory, filename))


if __name__ == "__main__":
    files = ["order_products__prior.csv", "products.csv"]
    logger.debug(f"Downloading {len(files)} files")

    shutil.rmtree('../data', ignore_errors=True)
    os.mkdir("../data")
    os.mkdir("../data/raw")
    os.mkdir("../data/processed")

    for file in files:
        download_file(directory="../data/raw", filename=file)


https://medium.com/codex/creating-a-multifaceted-grocery-recommender-system-c394208f5e0b
https://github.com/melodygr/grocery_recommendation
https://machinelearningmastery.com/using-singular-value-decomposition-to-build-a-recommender-system/



https://www.udemy.com/course/machinelearning/learn/lecture/19799886#overview
