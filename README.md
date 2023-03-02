
# Store YouTube Transcript/Subtitle to Mongo DB API (including automatically generated subtitles and subtitle translations)  

This is a python API which allows you to store mongo collection the transcript/subtitles for a given YouTube video. Using  [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/):

## Mongo Connection

mongo db connection and collection settings :
```
WATCH_URL = 'https://www.youtube.com/watch?v={video_id}'
MONGO_DB = 'youtubeTranscriptDB'
MONGO_DB_USERNAME = 'mongoadmin'
MONGO_DB_PASSWORD = 'secret'
MONGO_HOST = 'mongo' !! replace mongo host
MONGO_TRANSCRIPT_COLLECTION = 'transcript'
MONGO_YOUTUBE_COLLECTION = 'youtube'
```

If you want to use it from source, you'll have to install the dependencies manually:

```
pip install -r requirements.txt
```

## API

The easiest way to store a transcript for a given video is to execute:

```bash
curl -X POST http://localhost:5000/api/transcripts/PzqmxMjcyM0
```

This will return successful response looking somewhat like this:

```json
{"success": true}
```

In case of api error return response looks like this:

```json
{"error": "Subtitles are disabled for this video"}
```

### Docker Image Build
Build docker image :
```dockerfile
docker build --tag python-transcript-api .
```

```bash
 docker images
```

```text
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
python-transcript-api   latest    42471e8d9b06   58 seconds ago   154MB

```

### Docker Compose


```bash
docker-compose up 
```
