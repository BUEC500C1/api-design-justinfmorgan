import io
import tweepy
import keys
import urllib.request
import json
import sys

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
    fileName = "resources/imageFile.jpg"
    tweetText = ''
    tweetUrl = ''

    for tweet in tweepy.Cursor(api.search, q=searchTerm).items(50):
        try:
            # Grabbing the imageUrl, tweetText, and the tweetUrl from the tweepy JSON generated
            imageUrl = str(tweet._json['entities']['media'][0]['media_url_https'])
            tweetText = str(tweet._json['text'])
            tweetUrl = str(tweet._json['entities']['media'][0]['url'])
        except(tweepy.TweepError, KeyError):
            pass

    # Save the image at the URL to a file
    try:
        urllib.request.urlretrieve(imageUrl, fileName)
    except(ValueError):
        print("Unable to find an image associated with the terms requested.")
        sys.exit(1)

    return (imageUrl, fileName, tweetText, tweetUrl)

#### Analyzes an image file and outputs the labels to a list
def visionAnalysis(fileName):
    #####Vision Instantiations#######
    try:
        # Instantiates a Google vision client
        client = vision.ImageAnnotatorClient()
    except(DefaultCredentialsError):
        print("Invalid Google Cloud Credentials! Export your credentials!")
        sys.exit(1)

    try:
        # Loads the image into memory
        with io.open(fileName, 'rb') as image_file:
            content = image_file.read()
    except(FileNotFoundError):
        print("Unable to find the file you're trying to analyze!")
        sys.exit(1)

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels

def searchAndAnalyzeImage(keywords):
    # Search for the keywords
    imageTuple = searchTwitter(keywords)

    # Store the vision labels from the image analysis in a list
    labelList = visionAnalysis(imageTuple[1])

    # Iterate through said labels and output them as a JSON
    x = {
        "search string" : keywords,
        "image url" : imageTuple[0],
        "tweet text" : imageTuple[2],
        "tweet url" : imageTuple[3]
    }

    # List of all the label descriptions
    descriptionList = []
    for label in labelList:
        descriptionList.append(label.description)

    x['labels'] = descriptionList

    return json.dumps(x)