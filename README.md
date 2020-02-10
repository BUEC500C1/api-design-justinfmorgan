# EC500 Homework 2: API-Design

# Welcome to my Tweepy/Google Vision API!
The API design is fairly simple. Simply run the python program via "python main.py 'search term'" and replace 'search term' (keep the quotes) with whatever term you want to scour Twitter for! The program will then output a JSON containing information about the first tweet it found matching that both matched the search term and also contained an image. The JSON will contain the following information: Your search string, the image URL, the tweet text, the tweet URL, and a list of labels outputted by a Google Vision API analysis done on the image. The actual tweepVisionApi.py file can be imported just like any other api, and the functions within it can be called! Theoretically this API could be used to perform mass searches on twitter for images related to search terms, grab the google vision label data from those images, and then machine learning could be performed to recognize patterns depending on search terms (just an idea).

# Here's a photo of main.py in action:
<p align="center">
<img src="./resources/mainExample.png" width="55%" />
</p>

# API Information
The tweepyVisionApi.py file contains the following functions:

