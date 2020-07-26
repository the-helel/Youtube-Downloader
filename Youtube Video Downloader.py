from pytube import YouTube
from tqdm import tqdm

# Taking input URL from user
youtube_url = input("Please enter a YouTube link:")


# Creating Object
yt = YouTube(youtube_url)

# Title of Video
print("Title: " + yt.title)


# Duration of Video
print("Duration: " + str(yt.length))


# Thumbnail Url of Video
print("Thumbnail Link: " + yt.thumbnail_url)


# Description of vide
print("Description: " + yt.description)


# Views on Video
print("Views: " + str(yt.views))

# Checking Age Restriction
print("Age Restricted: " + str(yt.age_restricted))

# Getting Video ID
print("Video ID: " + yt.video_id)


# First Stream to Download
first_stream = yt.streams.first()
print("First Stream is " + str(first_stream))

# Path To Save Video ---You can add your own path 
savepath="C:/Users/Dell/Desktop/Django_work/"

# Progress bar 
for i in tqdm (first_stream.download(savepath)):
    pass
print("Success")