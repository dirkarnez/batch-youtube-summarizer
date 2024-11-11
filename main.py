import subprocess
import json
from argparse import ArgumentParser

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

parser = ArgumentParser()
parser.add_argument('-v', '--video-id')
args = parser.parse_args()

# video_id="AHyFar_R2K0" #"ilca5A9mLIA"
print(args.video_id)

transcript = YouTubeTranscriptApi.get_transcript(args.video_id)

formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
text_formatted = formatter.format_transcript(transcript).replace('\n', ' ')

print(text_formatted)

output = subprocess.run(
    [
        "curl", "-X", "POST", "https://syllaby.io/wp-json/api/v1/prompt", 
        "-H", "Content-Type: application/json", 
        "-d", f'{{"chrome_extension":true,"youtube_id":"{args.video_id}","transcript":"{text_formatted}","title":"XXXXXX - YouTube","bullet":false}}'
    ],
    capture_output=True
)

print(output)
a=json.loads(output.stdout)
print(a['data'][0]['summary'])
