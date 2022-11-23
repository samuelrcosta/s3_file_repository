import sys
import os
from datetime import datetime
from dotenv import load_dotenv


sys.path.append(".")
load_dotenv()

from file_uploader.repository.file_repository import FileRepository
from file_uploader.read import get_files
from file_uploader.config import LIST_LIMIT


if __name__ == "__main__":
    repository = FileRepository()

    files = get_files()[-LIST_LIMIT:]
    print(f"{datetime.now()} FOUND FILES", files)

    for file in files:
        print(f"{datetime.now()} Starting: {file}")
        try:
            repository.upload_file(file)
            os.remove(file)
            print(f"{datetime.now()} Finish success: {file}")
        except Exception as err:
            print(f"{datetime.now()} Error on: {file}", str(err))
    
