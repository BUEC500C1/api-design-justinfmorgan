import tweepy

import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)

# for tweet in public_tweets:
#     print(tweet._json['entities']['media'][0]['media_url_https'])

for tweet in tweepy.Cursor(api.search, q='tweepy cat').items(10):
    try:
        print(tweet._json['entities']['media'][0]['media_url_https'])
    except:
        pass

