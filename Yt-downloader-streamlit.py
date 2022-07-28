
from pytube import YouTube
from tkinter import filedialog
from streamlit import *
# from pytube.cli import on_progress
# from moviepy import *
# from moviepy.editor import VideoFileClip
from tkinter import *

import streamlit 
# import shutil


root = streamlit
# root.geometry('800x800')
root.title('Siwach Youtube video Downloader')

# def Download():


# try:
#     def func(default=''):
#         def Download():
#             video.download()
#             write(text='Downloading...', font=('Times',20,'normal'), fg='Red' ) 

         

#         url=link
        
#         try:
#             video = YouTube(url)
          
            
#         except:
#             write(text='Please Enter a valid Url') 
            
#         else:
#             video = video.streams.get_highest_resolution()
#             if button(Download):
#                 Download()
# except:
#     print('Error Occured')    



# welcome = Label(text='Youtube Video Downloader', fg='White', bg='Red', font=('Times',28,'normal'),width=22)
# welcome.place(relx=0.5, rely=0.155, anchor=CENTER)


# link = Entry(width = 20, borderwidth=3, font=('Times',24,'normal'), justify=CENTER, bg='yellow')
# link.insert(0, 'Enter Url')

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
            video.download()
            success('Download Started Please check video in your device folder..')
            warning('Thanks for using this website 😊') 
    



# link.place(relx=0.5, rely=0.275, anchor=CENTER)


# enter = Button(root, text='Enter', fg='White', bg='Red', font=('Times',16,'normal'), command=func)
# enter.place(relx=0.7, rely=0.275, anchor=CENTER)    
    

# # path_label = Label(text='Change Download Location ?', font=('TImes',20,'normal'), fg='Black')    
# # path_label.place(relx=0.5, rely=0.375, anchor=CENTER)
# # path_button = Button(root, text="Select", bg='red', padx='22', pady='5',font=('Arial', 18), fg='#fff', command=select_path)
# # path_button.place(relx=0.5, rely=0.45, anchor=CENTER)

# root.bind('<Return>',func)

# root.mainloop()