# youtube_scrape
This is a library for building playlists and scraping youtube videos. 

Insert the youtube playlist name and url and download to folder. Then, convert all videos to .mp4 format for further processing.

This is good for emotional labels (angry, happy, sad, etc.) to be further processed, or just any video with sounds that we'd like to look further into. 

# making playlists

To make a playlist:
    
    cd ~
    cd youtube_scrape 
    python3 make_playlist.py
    what is the playlist id?
    ...

This then makes a playlist from all the playlist ids. Note that only the first 100 in each playlist will be added to the playlist. Also, don't worry about duplicate video links in similar playlists (e.g. cnn videos); we take care of this by making sure no duplicate links go into the playlist. 

# downloading playlists generated 

Once you make a playlist, you can easily download it by:

    cd ~ 
    cd youtube_scrape
    python3 download_playlist.py 
    
This will then download the playlist and format it according to the style needed to train emotion detection models with train_emotions library.
 
 # references
 * [pytube](https://github.com/nficano/pytube)
 * [youtubedl](https://rg3.github.io/youtube-dl/)
