import logging
import pymongo
import json
from _settings import MONGO_DB_USERNAME
from _settings import MONGO_DB_PASSWORD
from _settings import MONGO_HOST
from _settings import MONGO_DB
from _settings import MONGO_TRANSCRIPT_COLLECTION
from _settings import MONGO_YOUTUBE_COLLECTION
from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

logger = logging.getLogger(__name__)
myClient = pymongo.MongoClient('mongodb://%s:%s@%s' % (MONGO_DB_USERNAME, MONGO_DB_PASSWORD, MONGO_HOST))
mydb = myClient[MONGO_DB]
transcript_collection = mydb[MONGO_TRANSCRIPT_COLLECTION]
youtube_collection = mydb[MONGO_YOUTUBE_COLLECTION]


@app.route('/api/transcripts/<string:youtube_id>', methods=['POST'])
def import_youtube_transcript_api(youtube_id):
    logger.info("importing youtube transcript for  %s", youtube_id)
    try:
        if youtube_collection.count_documents({'youtubeId': youtube_id}) > 0:
            logger.info("transcript already stored :  %s", youtube_id)
        else:
            transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
            data = {'transcript': transcript, 'youtubeId': youtube_id}
            youtube_collection.insert_one(data)
            result = [{**item, 'youtubeId': youtube_id} for item in transcript]

            transcript_collection.insert_many(result)
            logger.info("transcript stored : %s", youtube_id)

    except Exception as exception:
        logger.error("Error: " + exception.cause)
        return json.dumps({"error": exception.cause}), 404
    return json.dumps({"success": True}), 201


if __name__ == '__main__':
    app.run()
