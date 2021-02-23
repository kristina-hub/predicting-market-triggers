__author__ = "Sadaf Najam"
__version__ = "1.0.0"
__email__ = "sadaf.najam91@gmail.com"
__status__ = "development"

import tweepy
class TwitterData:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        print('Twitter API authenticated')

    def search(self, query, count, **kwargs):
        return tweepy.Cursor(self.api.search, q=query, count=200, lang='en', **kwargs).items(count)
