import sys
import os
from dotenv import load_dotenv


sys.path.append(".")
load_dotenv()

from file_uploader.repository.file_repository import FileRepository
from file_uploader.read import get_files


if __name__ == "__main__":
    repository = FileRepository()

    files = get_files()
    print("FOUND FILES", files)

    for file in files:
        print(f"Starting: {file}")
        try:
            repository.upload_file(file)
            os.remove(file)
            print(f"Finish success: {file}")
        except Exception as err:
            print(f"Error on: {file}", str(err))
    
