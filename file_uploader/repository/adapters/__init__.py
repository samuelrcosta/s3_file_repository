from abc import ABC, abstractmethod


class FileStorageAdapter(ABC):
    @abstractmethod
    def upload_file(self, bucket_name: str, local_file_path: str, remote_path: str):
        pass
