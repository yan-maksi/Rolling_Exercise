import cv2
import os


def open_images_from_folder(folder):
    """Give a image to, def is_frame_tagged()"""
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    print("Image opend from folder")
    return images