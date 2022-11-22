from file_uploader.config import B2_APPLICATION_KEY, B2_ENDPOINT, B2_KEY_ID
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
from file_uploader.repository.adapters import FileStorageAdapter


class B2FileStorage(FileStorageAdapter):
    def __init__(self) -> None:
        super().__init__()
        self._client = boto3.resource(
            service_name='s3',
            endpoint_url=B2_ENDPOINT,  # Backblaze endpoint
            aws_access_key_id=B2_KEY_ID,                # Backblaze keyID
            aws_secret_access_key=B2_APPLICATION_KEY,
            config=Config(
                signature_version='s3v4',
            )
        )

    def upload_file(self, bucket_name: str, local_file_path: str, remote_path: str):
        try:
            response = self._client.Bucket(bucket_name).upload_file(local_file_path, remote_path)
        except ClientError as ce:
            print('error', ce)

        return response
