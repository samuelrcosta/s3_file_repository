from glob import glob
from os import path
from file_uploader.config import LOCAL_DIR


def get_files():
    print(LOCAL_DIR)
    files = glob(f"{LOCAL_DIR}/**/*", recursive=True)
    files = [f for f in files if path.isfile(f)]
    return files
