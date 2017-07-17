from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

import os

DATABASE_URL = os.environ.get('DATABASE_URL', None)

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    def __repr__(self):
        return "<Artist(name='{}')>".format(self.name)


class Song(Base):
    __tablename__ = 'songs'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))

    # Relationships
    artist = relationship(Artist)

    def __repr__(self):
        return "<Song(name='{}', artist='{}')>".format(self.name, self.artist)

    def to_message(self):
        return '{} - {}: {}'.format(self.artist.name, self.name, self.url)


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
