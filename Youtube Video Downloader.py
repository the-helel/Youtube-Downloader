from pytube import YouTube
from tqdm import tqdm

# Taking input URL from user
youtube_url = input("Please enter a YouTube link:")


# Creating Object
youtube_obj = YouTube(youtube_url)

# Title of Video
print("Title: " + youtube_obj.title)


# Duration of Video
print("Duration: " + str(youtube_obj.length))


# Thumbnail Url of Video
print("Thumbnail Link: " + youtube_obj.thumbnail_url)


# Description of vide
print("Description: " + youtube_obj.description)


# Views on Video
print("Views: " + str(youtube_obj.views))

# Checking Age Restriction
print("Age Restricted: " + str(youtube_obj.age_restricted))

# Getting Video ID
print("Video ID: " + youtube_obj.video_id)


# First Stream to Download
first_stream = youtube_obj.streams.first()
print("First Stream is " + str(first_stream))

# Path To Save Video ---You can add your own path 
savepath="C:/Users/Dell/Desktop/Django_work/"

# Progress bar 
for i in tqdm (first_stream.download(savepath)):
    pass
print("Success")
