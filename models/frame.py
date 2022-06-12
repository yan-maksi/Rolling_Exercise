from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from consts import BASE


class Frame(BASE):
    __tablename__ = 'Frame'

    os_frame_path = Column(Text, primary_key=True)
    frame_index = Column(Integer)

    video = relationship('Video', back_populates='frame')
    video_name = Column(Text, ForeignKey('Video.video_name'))

    frame_metadata = relationship('Metadata', backref='frame_metadata')
    metadata_id = Column(Text, ForeignKey('Metadata.id'))
