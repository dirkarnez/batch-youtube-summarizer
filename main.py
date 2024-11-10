from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

transcript = YouTubeTranscriptApi.get_transcript("ilca5A9mLIA")

formatter = TextFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)

print(json_formatted)

import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'chrome_extension': True,
    'youtube_id': 'fdgd',
    'transcript': 'ReqBin Online Curl Client allows you to execute Curl commands directly in the browser, eliminating the need for external tools, and does not require the installation of any browser plug-ins or software on your computer.',
    'title': 'XXXXXX - YouTube',
    'bullet': False,
}

data = '{"chrome_extension":true,"youtube_id":"fdgd","transcript":"ReqBin Online Curl Client allows you to execute Curl commands directly in the browser, eliminating the need for external tools, and does not require the installation of any browser plug-ins or software on your computer.","title":"XXXXXX - YouTube","bullet":false}'
response = requests.post('https://syllaby.io/wp-json/api/v1/prompt', headers=headers, data=data)

# response = requests.post('https://syllaby.io/wp-json/api/v1/prompt', headers=headers, json=json_data)
# Print the response
print(response.status_code)
print(response.content)