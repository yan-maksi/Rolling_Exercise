import os
from azure.storage.blob import BlobServiceClient
from consts import BASE, ENGINE, CONNECTION_STRING
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from consts import LOCAL_BLOB_PATH


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    DBSession = sessionmaker(binds={BASE: ENGINE}, expire_on_commit=False)
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()


class AzureBlobFileDownloaderManager:
    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        self.my_container = self.blob_service_client.get_container_client('yan-hafifa')
        print("Intializing AzureBlobFileDownloader")

    def save_blob(self, FILE_NAME, file_content):
        download_file_path = os.path.join(LOCAL_BLOB_PATH, FILE_NAME)  # Get full path to the file
        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)  # for nested blobs, create local path as well!

        with open(download_file_path, "wb") as file:
            file.write(file_content)

    def download_all_blobs_in_container(self):
        my_blobs = self.my_container.list_blobs()
        for blob in my_blobs:
            print(blob.name)
            bytes = self.my_container.get_blob_client(blob).download_blob().readall()
            self.save_blob(blob.name, bytes)

