# pip install pytube3 for this script to run
#
#Script downloads the youtube playlist of AndrewNg from the Link -->>   https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN
#Script only downloads 100 videos (any additional logic will be appreciated) whereas the playlist contains 112 videos

import os
import time
print('Run this program in a virtualenv(program may install packages)')

print('Press CTRL+C to abort ')
time.sleep(5)
try:
	from pytube import YouTube
except:
	print('Installing pytube3')
	os.system('pip3 install pytube3')
	from pytube import YouTube

try:
	import re
	import requests 
	import json
	from urllib.request import Request,urlopen

except:print('Please install important modules as re,requests,json')

print( "\033[1m" + 'Initializing Download' +  "\033[0m")

#Change the Playlist Link below for different video playlist
playlist_link = 'https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN'
req = Request(playlist_link)
webpage = urlopen(req).read().decode('unicode_escape')  

link_dictionary = re.findall('window\["ytInitialData"\] = {.*}',webpage)

pattern =re.compile('(/watch\?v=\S+)')#regex expression to extract partial links from the window["ytInitialData"]

video_links = []

parent_link = 'https://www.youtube.com'

video_data = list((pattern.findall(link_dictionary[0])))

no_of_videos = len(video_data)
print(no_of_videos, 'videos to download')


video_links = []
for i in range(no_of_videos):
    video_links.append(parent_link + video_data[i].split(',')[0][:-6])
    
    
for i in video_links:
	try:
		video = YouTube(i)
		print(video.title)
		stream = video.streams.first()
		stream.download()
		
	except:print('Not a video...Preprocessing error')

#All 100 videos will be downloaded by the end of this	
 
