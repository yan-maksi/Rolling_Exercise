import cv2


def video_to_frames(path_to_video):
    """Split a video to folder Frames/TelAviv"""
    videoCapture = cv2.VideoCapture(path_to_video)
    videoCapture.open(path_to_video)
    frames_amount = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

    # fps = videoCapture.get(cv2.CAP_PROP_FPS)
    # print("fps=", int(fps), "frames=", int(frames_amount))

    for image_number in range(int(frames_amount)):
        _, frame = videoCapture.read()
        cv2.imwrite(f"data_collection/Frames/TelAviv/ {image_number}.jpg", frame)

    print("Video is splited")

    return int(frames_amount)


