
from pytube import YouTube

from streamlit import *
from pathlib import Path
downloads_path = str(Path.home() / "Downloads")

import streamlit 



root = streamlit

root.title('Siwach Youtube video Downloader')



      

link = text_input(label='Enter Url')
if link!='':
    url=link
        
    try:
        video = YouTube(url)
          
            
    except:
        write('Please Enter a valid Url') 
            
    else:
        video = video.streams.get_highest_resolution()
        if button(label='Download'):
            video.download(downloads_path)
            success('Download Started Please check video in your device folder..')
            warning('Thanks for using this website 😊') 
    



