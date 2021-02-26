from textblob import TextBlob
from sadaf_twitter.clean_tokens import CleanTokens
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
class SentimentAnalysis(object):
    def normalizing_tweets_data(self , list_of_tweets):
        collection = []
        clean_api = CleanTokens()
        for tweet in list_of_tweets:
            if tweet.get('retweet_count') in tweet and tweet.get('retweet_count')> 0:
                collection.append(clean_api.clean_noise(tweet.get('text'))) 
            else: 
                collection.append(clean_api.clean_noise(tweet.get('text')))
        tweet_txt_tokens = [sent_tokenize(txt) for txt in collection]
#         print(tweet_txt_tokens[1])
        txt_tokens = [item for token in tweet_txt_tokens for item in token]
#         print(txt_tokens[0])
        clean_api = CleanTokens()
        return clean_api.normalize_list_of_tweets(txt_tokens)
    
    def extract_analysis_data(self, sentiment_analysis_data):
        positive_tweets = [sentiment_info for sentiment_info in sentiment_analysis_data if sentiment_info['sentiment'] == 'positive']
        negative_tweets = [sentiment_info for sentiment_info in sentiment_analysis_data if sentiment_info['sentiment'] == 'negative']
        if (len(positive_tweets)/len(sentiment_analysis_data)) > \
            (len(negative_tweets)/len(sentiment_analysis_data)):
            return 'positive', positive_tweets, negative_tweets
        else:
            return 'negative', positive_tweets, negative_tweets
    
    def text_blob_score(self, tweet):
        analysis = TextBlob(tweet) 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
    
    def text_blob_analysis(self, list_of_tweets):
        collection = []
        for txt in list_of_tweets:
            collection.append({
                'text' : txt,
                'sentiment' : self.text_blob_score(txt)
            })
        return collection
    
    def get_text_blob_indication(self, list_of_tweets):
        sentiment_analysis_data = self.text_blob_analysis(self.normalizing_tweets_data(list_of_tweets))
        return self.extract_analysis_data(sentiment_analysis_data)
    
    def intensity_analyser_score(self, tweet):
        analyser = SentimentIntensityAnalyzer()
        analysis = analyser.polarity_scores(tweet)
        if analysis['compound'] >= 0.05: 
            return 'positive' 
        elif analysis['compound'] <= -0.05: 
            return 'negative'
        else:
            return 'neutral'

    def intensity_analyser_analysis(self, list_of_tweets):
        collection = []
        for txt in list_of_tweets:
            collection.append({
                'text' : txt,
                'sentiment' : self.intensity_analyser_score(txt)
            })
        return collection

    def get_intensity_analyser_indication(self, list_of_tweets):
        sentiment_analysis_data = self.intensity_analyser_analysis(self.normalizing_tweets_data(list_of_tweets))
        return self.extract_analysis_data(sentiment_analysis_data)