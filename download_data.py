"""Download the UCI Online Retail dataset into the local data folder."""

from pathlib import Path
from urllib.request import urlretrieve

DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
DATA_DIR = Path(__file__).resolve().parent / "data"
OUTPUT_FILE = DATA_DIR / "Online Retail.xlsx"


def download_dataset():
    """Create the data folder and download the Online Retail Excel file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if OUTPUT_FILE.exists():
        print("Dataset already exists at " + str(OUTPUT_FILE))
        return OUTPUT_FILE

    print("Downloading dataset from " + DATA_URL)
    urlretrieve(DATA_URL, OUTPUT_FILE)
    print("Dataset saved to " + str(OUTPUT_FILE))
    return OUTPUT_FILE


if __name__ == "__main__":
    download_dataset()
