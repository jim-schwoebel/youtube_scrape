'''
Extract playlist URLs
(for further processing)

'''
###########################################################################
#                       IMPORT STATEMENTS                                ##
###########################################################################
import requests, json, os 
from bs4 import BeautifulSoup
from pytube import YouTube

###########################################################################
#                       HELPER FUNCTIONS                                ##
###########################################################################
def scrapelinks(playlist, links):
    #https://www.youtube.com/playlist?list=PL1v-PVIZFDsqbzPIsEPZPnvcgIQ8bNTKS
    page=requests.get(playlist)
    base='https://www.youtube.com/watch?v='
    soup=BeautifulSoup(page.content, 'lxml')

    g=soup.find_all('tr',class_='pl-video yt-uix-tile ')
    entries=list()
    totaltime=0

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
            totaltime=totaltime+duration

            if link not in links:

                # avoids duplicate links 
                links.append(link)

                entry={
                    'title':title,
                    'link':link,
                    'duration':duration
                    }
                
                entries.append(entry)

        except:
            print('error')

    return entries, len(entries), totaltime, links

###########################################################################
##                          MAIN CODE BASE                               ##
###########################################################################

playlists=list()
entries=list()
t=1
totalnum=0
totaltime=0
links=list()

playlist_name=input('what do you want to name this playlist (e.g. angry)?')

while t>0:
    
    #try:

    playlist=input('what is the playlist id?')
    if playlist not in ['', 'n']:
        playlist='https://www.youtube.com/playlist?list='+playlist
        playlists.append(playlist)
        entry, enum, nowtime, link=scrapelinks(playlist, links)
        links=links+link 
        totalnum=totalnum+enum
        totaltime=totaltime+nowtime 
        entries=entries+entry
    else:
        break

    #except:

        #print('error') 

os.mkdir(playlist_name)
os.chdir(os.getcwd()+'/'+playlist_name)

data={
    'entrynum':totalnum,
    'total time':totaltime,
    'playlist url':playlists,
    'entries':entries,
}

jsonfile=open(playlist_name+'.json','w')
json.dump(data,jsonfile)
jsonfile.close()
