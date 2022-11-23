import os
from datetime import datetime
from glob import glob
from os import path
from file_uploader.config import LOCAL_DIR


WAIT_CREATED_SECONDS_TO_DOWNLOAD = 15


def if_valid_for_download(filename):
    t = os.path.getmtime(filename)
    now = datetime.now()
    modified = datetime.fromtimestamp(t)

    return (now - modified).seconds > WAIT_CREATED_SECONDS_TO_DOWNLOAD


def get_files():
    print(LOCAL_DIR)
    files = glob(f"{LOCAL_DIR}/**/*", recursive=True)
    files = [f for f in files if path.isfile(f) and if_valid_for_download(f)]
    return files
