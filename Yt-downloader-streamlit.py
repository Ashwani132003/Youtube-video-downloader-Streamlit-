
from pytube import YouTube

from streamlit import *
# from pathlib import Path
# downloads_path = str(Path.home() / "Downloads")

import streamlit 

import subprocess

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
            try:
                folder = subprocess.run(["xdg-user-dir", "DOWNLOAD"],
                            capture_output=True, text=True).stdout.strip("\n")
            except FileNotFoundError:  # if the command is missing
                import os.path
                folder = os.path.expanduser("~/Downloads") 
            video.download(folder)
            success('Download Started Please check video in your device folder..')
            warning('Thanks for using this website 😊') 
    



