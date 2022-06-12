from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()
ENGINE = create_engine("postgresql://postgres:12345678@localhost:5432/BionicEye", echo=True)

NAME = 'data_collection/TelAviv_15_06_34_12_06_00.mp4'

VIDEO_NAME = "TelAviv_15_06_34_12_06_00.mp4"

FILE_PATH = "data_collection/Frames/TelAviv"

PATH_OF_VIDEO = "data_collection/Video/TelAviv_15_06_34_12_06_00.mp4"
# Replace with the local folder where you want files to be downloaded

LOCAL_BLOB_PATH = "data_collection/Video/TelAviv_15_06_34_12_06_00.mp4"

# Replace with blob container
MY_BLOB_CONTAINER = "yan-hafifa"

CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=hafifaos;AccountKey=GYFMpijXyEmd3IIRPw0DnjH3EhNeUFkSHxtK1i7kiaNdX4vWvf9ijhtE9xGpTZmvPERUygc4N1Elccdf143qWg==;EndpointSuffix=core.windows.net"

FILE_NAME = "data_collection/Video"


# KEY: GYFMpijXyEmd3IIRPw0DnjH3EhNeUFkSHxtK1i7kiaNdX4vWvf9ijhtE9xGpTZmvPERUygc4N1Elccdf143qWg==
#
# Connection String: DefaultEndpointsProtocol=https;
#
# AccountName=hafifaos;
#
# AccountKey=GYFMpijXyEmd3IIRPw0DnjH3EhNeUFkSHxtK1i7kiaNdX4vWvf9ijhtE9xGpTZmvPERUygc4N1Elccdf143qWg==;
#
# EndpointSuffix=core.windows.net


