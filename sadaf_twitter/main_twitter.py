
from sadaf_twitter.api_twitter import TwitterAPI
import json
from sadaf_twitter.sentiment_analysis import SentimentAnalysis
import time
# 'Apple Inc' OR AAPL
class MainTwitter(object):
    def get_data(useAPI, stock):
        if useAPI :
            api = TwitterAPI()
            count = 100
            return api.read_tweets(count, stock)
        else:
            print('loading json data')
            f = open('datasets/api_twitter.json','r', encoding= 'utf-8')
            return json.load(f)
    def run(self,stock):
        response = self.get_data(True)
        sentimentanalysis = SentimentAnalysis()
        indication, positive_tweets, negative_tweets = sentimentanalysis.get_indication(response)  
        if (indication == 'positive'):
            print(indication, " market triggers indicate that you should buy this stock")
            return 1
        else:
            print(indication, " market triggers indicate that you should not buy this stock")
            return 0
    
    if __name__ == "__main__":
        response = get_data(True)
        sentimentanalysis = SentimentAnalysis()
        indication, positive_tweets, negative_tweets = sentimentanalysis.get_indication(response)  
#         indication, positive_tweets, negative_tweets = sentimentanalysis.get_intensity_analyser(response)  
        if (indication == 'positive'):
            print(indication, " market triggers indicate that you should buy this stock")
        else:
            print(indication, " market triggers indicate that you should not buy this stock")
#         print()
#         for tweet in positive_tweets: 
#             print(tweet['text'].encode('ascii', 'ignore')) 
#         print()     
#         for tweet in negative_tweets: 
#             print(tweet['text'].encode('ascii', 'ignore')) 
            
#         print()
#         test_tweet = [{"text": "Apple is being treated as the biggest ATM in the world Berkshire Hathaway's best decision last decade could bite " }]
#         indication, positive_tweets, negative_tweets = sentimentanalysis.get_indication(test_tweet)
#         print(indication, " sentence")
#         print()
#         time.sleep(5)
# 
#         test_tweet = [{"text": "PC/MAC sales of Apple could tank this year, since a lot of demand was pulled forward last year due to WFH" }]
#         indication, positive_tweets, negative_tweets = sentimentanalysis.get_indication(test_tweet)
#         print(indication, " sentence")
    