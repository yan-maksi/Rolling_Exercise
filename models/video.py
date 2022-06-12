from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from consts import BASE


class Video(BASE):
    __tablename__ = 'Video'

    video_name = Column(Text, primary_key=True)
    video_path = Column(Text)
    frame_amount = Column(Integer)
    frame = relationship('Frame', back_populates='video')
