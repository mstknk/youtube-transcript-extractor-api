import logging
import json
from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/api/transcripts/<string:youtube_id>', methods=['POST'])
def youtube_transcript_api(youtube_id):
    logger.info("getting transcript for youtubeId %s", youtube_id)
    try:
        transcript = YouTubeTranscriptApi.get_transcripts([youtube_id], languages=['de'])
    except Exception as exception:
        logger.error("Error: " + exception.cause)
        return json.dumps({"error": exception.cause}), 404
    return json.dumps({"result": transcript}), 201


if __name__ == '__main__':
    app.run()
