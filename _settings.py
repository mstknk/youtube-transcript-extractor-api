import os
from dotenv import load_dotenv
load_dotenv()

WATCH_URL = os.environ.get("WATCH_URL")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_DB_USERNAME = os.environ.get("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD = os.environ.get("MONGO_DB_PASSWORD")
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_TRANSCRIPT_COLLECTION = os.environ.get("MONGO_TRANSCRIPT_COLLECTION")
MONGO_YOUTUBE_COLLECTION = os.environ.get("MONGO_YOUTUBE_COLLECTION")
