import tweepy
import json
class TwitterAPI:
    def __init__(self):
        consumer_key = 'vKw3DGGkKEKx9is4d11zRzm2n'
        consumer_secret='kvBll57qOpzyS7ryIGNGg74llQrHJEhoHBL940iEwHPKdLSJKg'
        access_token = '860140613467033600-9ZQyZCunQ3z0USEl03ASx7qkMGfL4u9'
        access_token_secret = 'LMeUgg71nMUSFJStzaNMPV2bTPbgEFDkzWd9ORlDSAQQ3'
        
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        print('Twitter API authenticated')

    def read_tweets(self, count, stock):
#         print("Recommended Entry Formats :: 'Apple Inc' OR AAPL || 'Microsoft Corporation' OR Microsoft OR MSFT")
#         stock = input('Enter Stock: ')
#         print('Processing market triggers for ' + stock)
        response =  [status._json for status in tweepy.Cursor(self.api.search,
                                                              q=stock, count=200, 
                                                              lang='en').items(count)]
        
        with open('sadaf_twitter/datasets/api_twitter.json', 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)

        return response