
from sadaf_twitter.api_twitter import TwitterAPI
import json
from sadaf_twitter.sentiment_analysis import SentimentAnalysis
import time
# 'Apple Inc' OR AAPL
class MainTwitter(object):
    def get_data(self, useAPI=True, stock="'Apple Inc' OR AAPL"):
        if useAPI :
            api = TwitterAPI()
            count = 1000
            return api.read_tweets(count, stock)
        else:
            print('loading json data')
            f = open('datasets/api_twitter.json','r', encoding= 'utf-8')
            return json.load(f)
    def run(self,stock):
        response = self.get_data(True, stock)
        sentimentanalysis = SentimentAnalysis()
        indication, positive_tweets, negative_tweets = sentimentanalysis.get_intensity_analyser_indication(response)  
        if (indication == 'positive'):
            print(indication, " market triggers indicate that you should buy this stock")
            return 1
        else:
            print(indication, " market triggers indicate that you should not buy this stock")
            return 0
    
    if __name__ == "__main__":
        response = get_data(False)
        sentimentanalysis = SentimentAnalysis()
#         indication, positive_tweets, negative_tweets = sentimentanalysis.get_text_blob_indication(response)  
        indication, positive_tweets, negative_tweets = sentimentanalysis.get_intensity_analyser_indication(response)  
        if (indication == 'positive'):
            print(indication, " market triggers indicate that you should buy this stock")
        else:
            print(indication, " market triggers indicate that you should not buy this stock")
#         print()
#         for tweet in positive_tweets: 
#             print(tweet['text']) 
#         print()     
#         for tweet in negative_tweets: 
#             print(tweet['text']) 
            
#         print()
#         test_tweet = [{"text": "Apple is being treated as the biggest ATM in the world Berkshire Hathaway's best decision last decade could bite " }]
#         indication, positive_tweets, negative_tweets = sentimentanalysis.get_intensity_analyser_indication(test_tweet)
# #         indication, positive_tweets, negative_tweets = sentimentanalysis.get_text_blob_indication(test_tweet)
#         print('before analysis : ' , test_tweet[0].get('text'))
#         print('after analysis : ' , positive_tweets[0].get('text'))
#         print('The above sentence is identified as "', indication, '" sentence')
#         print()
#         time.sleep(5)
#   
#         test_tweet = [{"text": "PC/MAC sales of Apple could tank this year, since a lot of demand was pulled forward last year due to WFH" }]
#         indication, positive_tweets, negative_tweets = sentimentanalysis.get_intensity_analyser_indication(test_tweet)
# #         indication, positive_tweets, negative_tweets = sentimentanalysis.get_text_blob_indication(test_tweet)
#         print('before analysis : ' , test_tweet[0].get('text'))
#         print('after analysis : ' ,negative_tweets[0].get('text'))
#         print('The above sentence is identified as "', indication, '" sentence')
    