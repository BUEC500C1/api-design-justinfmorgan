import io
# import os
import sys
import tweepy
import keys
import urllib.request
import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.auth.exceptions import DefaultCredentialsError

#####Tweepy API Authentication stuff#######
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

### Use Tweepy to search twitter for the first image with a tweet related to the search term
def searchTwitter(searchTerm):
    #####Getting the image URL from Tweepy#####
    imageUrl = ''
    fileName = "imageFile.jpg"

    for tweet in tweepy.Cursor(api.search, q=searchTerm).items(10):
        try:
            # print(tweet._json['entities']['media'][0]['media_url_https'])
            imageUrl = str(tweet._json['entities']['media'][0]['media_url_https'])
        except(tweepy.TweepError, KeyError):
            pass

    print(imageUrl)

    # Save the image at the URL to a file
    try:
        urllib.request.urlretrieve(imageUrl, fileName)
    except(ValueError):
        print("Unable to find an image associated with the terms requested.")
        sys.exit(1)

    return (imageUrl, fileName)

#### Analyzes an image file and outputs the labels to a JSON
def visionAnalysis(fileName):
    #####Vision Instantiations#######
    try:
        # Instantiates a Google vision client
        client = vision.ImageAnnotatorClient()

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
    except(DefaultCredentialsError):
        print("Invalid Google Cloud Credentials! Export your credentials!")
        sys.exit(1)
    return None

def searchAndAnalyzeImage(keywords):
    imageTuple = searchTwitter(keywords)
    visionAnalysis(imageTuple[1])

def main():
    #CHECK ARGUMENTS!
    if(len(sys.argv) < 2):
        print("Please provide a search term argument in quotes")
        sys.exit(1)
    else:
        searchAndAnalyzeImage(sys.argv[1])

if __name__ == "__main__":
    main()