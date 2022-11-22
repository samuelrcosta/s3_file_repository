from os import path
from file_uploader.config import BUCKET_NAME
from file_uploader.repository.adapters.b2_adapter import B2FileStorage


class FileRepository:
    def __init__(self) -> None:
        self.adapter = B2FileStorage()
        self.bucket = BUCKET_NAME

    def upload_file(self, local_file_path: str):
        path_parts = local_file_path.split("/")
        remote_path_parts = path_parts[-3:]
        remote_path = "/".join(remote_path_parts)
        return self.adapter.upload_file(self.bucket, local_file_path, remote_path)
