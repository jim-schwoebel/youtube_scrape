# youtube_scrape
This is a library for building playlists and scraping youtube videos. 

![](https://media.giphy.com/media/tZ0J66Y9fOzG8/giphy.gif)

All you need to do is insert the youtube playlist name and url and it will download the playlist to a folder. All videos are converted to .mp4 format for further processing.

These scripts are good for labeling videos on YouTube (angry, happy, sad, etc.) to be further processed by machine learning models.

## making playlists

To begin making a playlist:
    
    cd ~
    cd youtube_scrape 
    python3 make_playlist.py
    what is the playlist id or URL?
    ...

Also, you can stop building your playlist and have it written to json by typing in nothing ('') or 'n'. 
The make_playlist.py script then makes a playlist from all the playlist ids or URLs that you have entered.

### what is the playlist ID?
Note that playlist IDs are readily accessible on YouTube as the id part of the URL. For example, https://www.youtube.com/watch?v=xPU8OAjjS4k&list=PLpoUYdDxb6P56t8lnxnA412k_H5EMHd-8 --> Playlist id is PLpoUYdDxb6P56t8lnxnA412k_H5EMHd-8. 

You don't need to necessarily put in the playlist ID for this script to work; you can also put the full playlist URL (e.g. https://www.youtube.com/playlist?list=PL1v-PVIZFDsqbzPIsEPZPnvcgIQ8bNTKS). 

Also, only the first 100 in each playlist will be added to the master playlist. Don't worry about duplicate video links in similar playlists (e.g. cnn videos); the script takes care of this by making sure no duplicate links go into the playlist. 

## downloading playlists generated 

Once you make a playlist, you can easily download it by:

    cd ~ 
    cd youtube_scrape
    python3 download_playlist.py 
    
You can then state the playlist in the /playlists folder that you'd like to download as either the name or .JSON file (e.g. 
yc_podcast or yc_podcast.json will work). 

The script will then download the playlist and format it according to the style needed to train machine learning models.
 
 # references
 * [pytube](https://github.com/nficano/pytube)
 * [youtubedl](https://rg3.github.io/youtube-dl/)
