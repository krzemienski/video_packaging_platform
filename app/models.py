__author__ = "The One & Only Javi"
__version__ = "1.0.0"
__start_date__ = "25th July 2020"
__end_date__ = "3rd August 2020"
__maintainer__ = "me"
__email__ = "little_kh@hotmail.com"
__requirements__ = "SQL-Alchemy, MySQL, Flask-SQLAlchemy, database script"
__status__ = "Production"
__description__ = """
This is the Database models script. Very important as it will
connect the database and map it with our model for this App
"""

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from database import metadata, db_session


class VideosDB(object):
    query = db_session.query_property()

    def __init__(self, *params):
        for name, value in zip(("input_content_id", "input_content_origin",
                                "video_track_number", "status",
                                "output_file_path", "video_key", "kid",
                                "packaged_content_id", "url"
                                ), tuple(params)):
            setattr(self, name, None)

    def __repr__(self):
        return '<VideosDB %r>' % (self.input_content_id)


uploaded_videos = Table('uploaded_videos', metadata,
                        Column('input_content_id', Integer, primary_key=True,
                               autoincrement=True, unique=True),
                        Column('input_content_origin', String(255), ),
                        Column('video_track_number', Integer),
                        Column('status', String(255)),
                        Column('output_file_path', String(255)),
                        Column('video_key', String(255)),
                        Column('kid', String(255)),
                        Column('packaged_content_id', Integer, unique=True),
                        Column('url', String(255))
                        )

mapper(VideosDB, uploaded_videos)
