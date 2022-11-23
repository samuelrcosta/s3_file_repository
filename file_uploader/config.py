from os import environ


LOCAL_DIR = environ.get("LOCAL_DIR")
BUCKET_NAME = environ.get("BUCKET_NAME")
B2_ENDPOINT = environ.get("B2_ENDPOINT")
B2_KEY_ID = environ.get("B2_KEY_ID")
B2_APPLICATION_KEY = environ.get("B2_APPLICATION_KEY")

LIST_LIMIT = environ.get("LIST_LIMIT", 20)
