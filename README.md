
# Store YouTube Transcript/Subtitle (including automatically generated subtitles and subtitle translations)  

This is a python API which allows you to get the german transcript/subtitles for a given YouTube video. Using  [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/):


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
{
	"result": [{
			"PzqmxMjcyM0": [{
					"text": "schon Zuschauer gedenken zum einen der",
					"start": 0.06,
					"duration": 3.78
				},
				{
					"text": "Opfer der zivilen wie auch der",
					"start": 2.34,
					"duration": 4.559
				}
			]
		},
		[]
	]
}
```

In case of api error return response looks like this:

```json
{"error": "Subtitles are disabled for this video"}
```

### Docker Image Build
Build docker image :
```dockerfile
docker build --tag youtube-transcript-extractor-api .
```

```bash
 docker images
```

```text
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
python-transcript-extractor-api   latest    42471e8d9b06   58 seconds ago   154MB

```

### Docker run container

```text
docker run -p 5000:5000 -d youtube-transcript-extractor-api
```
