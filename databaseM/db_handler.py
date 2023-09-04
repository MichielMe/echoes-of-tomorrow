##### --------------------- MONGODB --------------------- #####

# from pymongo.mongo_client import MongoClient
# from dotenv import load_dotenv
# import os

# load_dotenv()
# uri = os.getenv("MONGODB_URI")

# client = MongoClient(uri)
# db = client.storytelling_mastodon
# stories = db.stories

# def save_new_chunk(new_chunk):
#     stories.insert_one({"chunk": new_chunk})

# def get_last_story_chunk():
#     last_story = stories.find_one(sort=[("_id", -1)])
#     return last_story["chunk"] if last_story else None



##### --------------------- SQLITE --------------------- #####
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, Sequence('story_id_seq'), primary_key=True)
    chunk = Column(String(500))

engine = create_engine('sqlite:///stories.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def save_new_chunk(new_chunk):
    story = Story(chunk=new_chunk)
    session.add(story)
    session.commit()

def get_last_story_chunk():
    last_story = session.query(Story).order_by(Story.id.desc()).first()
    return last_story.chunk if last_story else None

save_new_chunk("This is a test for my story")