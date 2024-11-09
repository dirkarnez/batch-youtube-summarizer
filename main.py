from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

transcript = YouTubeTranscriptApi.get_transcript("ilca5A9mLIA")

formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)

print(json_formatted)

import requests

 
# data = '{
#     'chrome_extension': True,
#     'youtube_id': 'ilca5A9mLIA',
#     'transcript': json_formatted,
#     'title': 'dummy title',
#     'bullet': 'false' }'
 
## post的时候，使用json参数
response = requests.post(url='https://syllaby.io/wp-json/api/v1/prompt', headers={"Content-Type": "application/json; charset=utf-8"}, data='{"chrome_extension":true,"youtube_id":"rAyMr0CWQ3U","transcript":"Free Youtube transcript summaries with our new Chrome extension!","title":"XXXXXX - YouTube","bullet":false}')

print(response.status_code)
print(response.content)