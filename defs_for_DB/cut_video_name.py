import re


def cut_video_name(full_video_name):
    """Deletes everything except the file name"""
    char = "".join(re.findall("[a-zA-Z]+", full_video_name))
    print("Video Name is cuted")
    return str(char[:-2])



