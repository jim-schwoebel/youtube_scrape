'''
Extract playlist URLs
(for further processing)
'''
import requests
from bs4 import BeautifulSoup

base='https://www.youtube.com/watch?v='

playlist=input('what is the playlist url?')
#https://www.youtube.com/playlist?list=PL1v-PVIZFDsqbzPIsEPZPnvcgIQ8bNTKS
page=requests.get(playlist)
soup=BeautifulSoup(page.content, 'lxml')

g=soup.find_all('tr',class_='pl-video yt-uix-tile ')
entries=list()
links=list()

for i in range(len(g)):
    try:
        h=str(g[i])
        
        # get titles
        h1=h.find('data-title="')+len('data-title="')
        h2=h[h1:].find('"')
        title=h[h1:h1+h2]

        # get links
        h3=h.find('data-video-id="')+len('data-video-id="')
        h4=h[h3:].find('"')
        link=base+h[h3:h3+h4]

        # get duration (in seconds)
        h5=h.find('<div class="timestamp"><span aria-label="')
        h6=h[h5:]
        hsoup=BeautifulSoup(h6,'lxml')
        htext=hsoup.text.replace('\n','').replace(' ','')
        hmin=htext.split(':')
        duration=int(hmin[0])*60+int(hmin[1])

        entry={
            'title':title,
            'link':link,
            'duration':duration
            }
        
        entries.append(entry)

    except:
        print('error')


    

    
