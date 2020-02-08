import io
# import os
import sys
import tweepy
import keys
import urllib.request

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#CHECK ARGUMENTS!
if(len(sys.argv) < 2):
    print("Please provide a search term argument in quotes")
    sys.exit(0)

#####Tweepy API Authentication stuff#######
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

# Used to get the tweets from my own page
# public_tweets = api.home_timeline()

#####Getting the image URL from Tweepy#####
imageUrl = ''

for tweet in tweepy.Cursor(api.search, q=sys.argv[1]).items(10):
    try:
        # print(tweet._json['entities']['media'][0]['media_url_https'])
        imageUrl = str(tweet._json['entities']['media'][0]['media_url_https'])
    except(tweepy.TweepError, KeyError):
        pass

print(imageUrl)

fileName = "imageFile.jpg"

# Save the image at the URL to a file
try:
    urllib.request.urlretrieve(imageUrl, fileName)
except(ValueError):
    print("Unable to find an image associated with the terms requested.")
    sys.exit(0)

#####Vision Instantiations#######
# Instantiates a client
client = vision.ImageAnnotatorClient()

# # The name of the image file to annotate
# file_name = os.path.abspath(imageUrl)

# Loads the image into memory
with io.open(fileName, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

#Prints out the descriptions for the image
print('Labels:')
for label in labels:
    print(label.description)