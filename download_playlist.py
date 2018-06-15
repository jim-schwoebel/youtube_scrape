'''
download_playlist.py

Download a playlist from the URLS previously generated
with make_playlist.py script.

Note: make sure you have at least around 10GB of disk space
before bulk downloading videos, as they can take up a lot of space.
'''
import requests, json, os 
from bs4 import BeautifulSoup
from pytube import YouTube

playlist_name=input('what is the name of the playlist?')
hostdir=os.getcwd()
os.chdir(playlist_name)

g=json.load(open(playlist_name+'.json'))
entries=g['entries']
links=list()

for i in range(len(entries)):
    link=entries[i]['link']
    links.append(link)

# download files 
for i in range(len(links)):
    try:
        link=links[i]
        print('downloading %s'%(link))
        YouTube(link).streams.first().download()
    except:
        print('error')

# rename videos in order
listdir=os.listdir()
for i in range(len(listdir)):
    if listdir[i][-5:] in ['.webm']:
        os.rename(listdir[i],str(i)+'.webm')
        os.system('ffmpeg -i %s %s'%(str(i)+'.webm',str(i)+'.mp4'))
        os.remove(str(i)+'.webm')
    elif listdir[i][-4:] in ['.mp4']:
        os.rename(listdir[i],str(i)+'.mp4')

# now make audio for each .mp4 file 
listdir=os.listdir()

for i in range(len(listdir)):
    if listdir[i][-4:]=='.mp4':
        os.system('ffmpeg -i %s %s'%(listdir[i],listdir[i][0:-4]+'.wav'))