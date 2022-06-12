from sqlalchemy import Column, Integer, Boolean, Text

from consts import BASE


class Metadata(BASE):
    __tablename__ = 'Metadata'

    id = Column(Text, primary_key=True)
    frame_label = Column(Boolean)
    azimuth = Column(Integer)
    elevation = Column(Integer)
    fov = Column(Integer)
