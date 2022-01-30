'''
================================================ 
          YOUTUBE_SCRAPE REPOSITORY                     
================================================ 

repository name: youtube_scrape 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/youtube_scrape 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: Library for scraping youtube videos. Alternative to pafy, pytube, and youtube-dl. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-07-23 

This code (youtube_scrape) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
                LICENSE TERMS                      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
                SERVICE STATEMENT                    
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in kafka distributed architectures, microservices 
built on top of Node.JS / python / docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
                    NOTE                  
================================================ 
Download a playlist from the URLS previously generated
with make_playlist.py script.

Make sure you have at least around 10GB of disk space
before bulk downloading videos, as they can take up a lot of space.

'''
import requests, json, os, time 
from bs4 import BeautifulSoup
from pytube import YouTube
import uuid, shutil
 
def scrapelinks(playlistid):
    print(playlistid)
    os.system('youtube-dl --rm-cache-dir')
    os.system('youtube-dl --extract-audio --audio-format wav --yes-playlist "%s" --sleep-interval 10'%(playlistid))

os.chdir('playlists')
print('Which playlist would you like to download?')
print('-----------------')
listdir=os.listdir()
for playlist in listdir:
    print(playlist)
print('-----------------')
playlist=input('?????? (include .json - e.g. jim.json) ????????\n')

if playlist not in listdir:
    print('ERROR - playlist does not exist')
else:
    playlistname=playlist.replace('.json','')
    load=json.load(open(playlist))['playlist url']
    try:
        os.mkdir(playlistname)
        os.chdir(playlistname)
    except:
        shutil.rmtree(playlistname)
        os.mkdir(playlistname)
        os.chdir(playlistname)    
    
    for urls in load:
        playlistid_index=urls.find('list=')
        playlistid=urls[(playlistid_index+5):]
        scrapelinks(playlistid)

    # now convert all the files with new names
    listdir=os.listdir()
    for file in listdir:
        if file.endswith('.wav'):
            os.rename(file, str(uuid.uuid4())+'.wav')
        else:
            os.remove(file)

    # now convert everything to mono 16000 Hz 
    listdir=os.listdir()
    for file in listdir:
        if file.endswith('.wav'):
            os.system('ffmpeg -i %s -acodec pcm_s16le -ac 1 -ar 16000 %s -y'%(file, 'cleaned_'+file))
            os.remove(file)