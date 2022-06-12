### Video column ###
from consts import NAME, VIDEO_NAME, PATH_OF_VIDEO, FILE_PATH
from defs_for_DB.cut_video_name import cut_video_name
from defs_for_DB.open_images_from_folder import open_images_from_folder
from defs_for_DB.split_video import video_to_frames

### Frame column ###
from os import listdir
from os.path import isfile, join


def video_column():
    video_name_cut = cut_video_name(VIDEO_NAME)  # Cut a video name: _TelAviv_ ->  TelAviv
    amount_of_frames = video_to_frames(PATH_OF_VIDEO)  # Extract frames from video
    video_path = NAME  # Extract frames from video
    return video_name_cut, amount_of_frames, video_path


def frame_column():
    # Open file, give a list file to loop them and upload to DB
    file_names = [file_name for file_name in listdir(FILE_PATH) if isfile(join(FILE_PATH, file_name))]
    os_frame_path = [f'Frames/{VIDEO_NAME}/{fn}' for fn in file_names]  # Give a path of file in OS
    video_frames = open_images_from_folder(FILE_PATH)  # Open all images from folder, give a list
    return file_names, os_frame_path, video_frames



# ### MetaData column ###
# import uuid
# from metadata_utils import is_frame_tagged, generate_metadata
#
#
# def meta_data_column():
#     def frame():
#         for frame in enumerate(frame_column.video_frames):
#             return frame
#
# metadata_id = str(uuid.uuid1())  # Give a uni cue ID to Metadata id frame_label_bool = is_frame_tagged(frame)  #
# return true or false, id in frame attend scull or not fov, azimuth, elevation = generate_metadata(
# frame_column.video_frames)  # return fov, azimuth and elevation for frame return metadata_id, frame_label_bool,
# fov, azimuth, elevation
