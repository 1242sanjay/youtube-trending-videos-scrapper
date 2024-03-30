import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

# requests does not execute javascript
response = requests.get(YOUTUBE_TRENDING_URL)

print('Status code ', response.status_code)
# print('Output', response.text[0:1000])

# with open('trending.html', 'w') as f:
#   f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
print('Page title ', doc.title)

# find all the video divs
video_divs = doc.find_all('div', class_='ytd-video-renderer')
print(f'Found {len(video_divs)} videos')
