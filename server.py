import os
from azure.storage.blob import BlobClient
from flask import Flask
from consts import CONNECTION_STRING, PATH_OF_VIDEO
from db_manager import session_scope, AzureBlobFileDownloaderManager
from models.frame import Frame
# from azure.storage import BlockBlobService
from pj_admin import traversing_all_frames

app = Flask(__name__)





@app.route("/")
def process_video():
    # AzureBlobFileDownloaderManager()  # Upload video to os
    # # 'Video uploaded to OS'
    # traversing_all_frames()  # Upload columns with data
    # # 'Uploaded columns with data to Pj Admin'

    # Upload frames to os
    def upload_file(remote_path, local_path):
        try:
            from azure.storage.blob import BlobClient

            blob = BlobClient.from_connection_string("my_connection_string", container="mycontainer", blob="my_blob")
            with open(PATH_OF_VIDEO, "rb") as data:
                blob.upload_blob(data)

        except Exception as e:
            raise Exception(f'Unable to save azure blob data. {str(e)}')



    # blob = BlobClient.from_connection_string(CONNECTION_STRING, container='yan-hafifa', blob='Frames')
    # upload_file_path = os.path.join('data_collection/Frames/TelAviv')
    #
    # with open(upload_file_path, "rb") as data:
    #     blob.upload_blob(data)

#################################################################################

@app.route("/get-all-video-paths")
def get_all_video_path():
    with session_scope() as sess:
        vide_names = sess.query(Frame.frame_index).all()

    return f'All file names: {vide_names}'


#################################################################################

@app.route('/get-specific-video-path/<frame_number_in_video>')
def get_specific_path_video(frame_number_in_video):
    with session_scope() as sess:
        result = sess.query(Frame).filter(Frame.frame_index.like(frame_number_in_video)).all

    return f'print your frame number: {result}'


#################################################################################

@app.route('/get-frame-path-of-video-specific/<video_name_in_db>')
def get_frame_path_of_video_specific(video_name_in_db):
    with session_scope() as sess:
        result = sess.query(Frame).filter(Frame.video_name.like(video_name_in_db)).first()
    return f'print your frame number: {result}'


#################################################################################


@app.route('/get-specific-frame-path-of-video/<video_name_in_db>/<number_frame>')
def get_specific_frame_path_of_video(video_name_in_db, number_frame):
    with session_scope() as sess:
        result = sess.query(Frame).filter(Frame.video_name.like(video_name_in_db)).first()
        number_frame = sess.query(Frame).filter(Frame.frame_index.like(number_frame)).first()
    return f'print your frame number: {result}, {number_frame}'


#################################################################################


@app.route('/download-video-from-os/<video_name_in_db>')
def get_specific_path_video_from_os(video_name_in_db):
    BLOB = BlobClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        container_name='yan-hafifa',
        blob_name=f'Video/{video_name_in_db}')

    file_data = video_name_in_db.split('.')[0] + '.mp4'
    print(file_data)

    with open(file_data, "wb") as my_blob:
        blob_data = BLOB.download_blob()
        blob_data.readinto(my_blob)
        file_new_name = video_name_in_db
        os.rename(str(file_data), str(file_new_name))

    return f'Your video is: {file_data}', file_data


################################################################################


@app.route('/get-frame-label-from-os/<name_of_video_in_db>')
def get_frame_label_from_os(name_of_video_in_db):
    BLOB = BlobClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        container_name='yan-hafifa',
        blob_name=f'Frames/{name_of_video_in_db}')

    download_file_path = os.path.join('yan-hafifa', f'Frames/{name_of_video_in_db}')
    os.makedirs(os.path.dirname(download_file_path), exist_ok=True)

    with open(download_file_path, "wb") as file:
        blob_data = BLOB.download_blob()
        blob_data.readinto(file)
        file.write(name_of_video_in_db)

    return f'The Blob {name_of_video_in_db} Saved', name_of_video_in_db


################################################################################

if __name__ == "__main__":
    app.run(debug=True)
