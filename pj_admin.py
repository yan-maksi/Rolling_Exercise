import uuid
from db_manager import session_scope
from defs_for_DB.columns_varible import frame_column, video_column
from consts import BASE, ENGINE
from defs_for_DB.metadata_utils import is_frame_tagged, generate_metadata
from models.video import Video
from models.frame import Frame
from models.Metadata import Metadata


def traversing_all_frames():
    """Creates columns in the database. And loads them into the database"""
    BASE.metadata.drop_all(ENGINE)
    BASE.metadata.create_all(ENGINE)

    video_name_cut, amount_of_frames, video_path = video_column()
    file_names, os_frame_path, video_frames = frame_column()

    with session_scope() as sess:
        sess.add(Video(video_name=video_name_cut,
                       video_path=video_path,
                       frame_amount=amount_of_frames))

        # Goes through all the frames in the Loop
        for index, frame in enumerate(video_frames):
            ### MetaData column ###
            metadata_id = str(uuid.uuid1())  # Give a uni cue ID to Metadata id
            frame_label_bool = is_frame_tagged(frame)  # return true or false, id in frame attend scull or not
            fov, azimuth, elevation = generate_metadata(video_frames)  # return fov, azimuth and elevation for frame

            sess.add(Metadata(id=metadata_id,
                              frame_label=frame_label_bool,
                              azimuth=azimuth,
                              elevation=elevation,
                              fov=fov))

            sess.add(Frame(os_frame_path=os_frame_path[index],
                           frame_index=index,
                           video_name=video_name_cut,
                           metadata_id=metadata_id))