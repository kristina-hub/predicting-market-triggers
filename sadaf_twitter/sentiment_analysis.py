from textblob import TextBlob
from sadaf_twitter.clean_tokens import CleanTokens
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalysis(object):
    def get_polarity(self, tweet):
        analysis = TextBlob(tweet) 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
    
    def prepare_sentiment_analysis(self, data):
        collection = []
        for tweet in data:
                parsed_data = {}
                clean_api = CleanTokens()
                cleaned_text = clean_api.clean_noise(tweet.get('text'))
                parsed_data['text'] = cleaned_text
                parsed_data['sentiment'] = self.get_polarity(cleaned_text)
                if tweet.get('retweet_count') in tweet and tweet.get('retweet_count')> 0:
                    if parsed_data not in collection: 
                        collection.append(parsed_data) 
                else: 
                    collection.append(parsed_data)
        return collection
    
    def get_indication(self, data):
        sentiment_analysis_data = self.prepare_sentiment_analysis(data)
        positive_tweets = [tweet_info for tweet_info in sentiment_analysis_data if tweet_info['sentiment'] == 'positive']
        negative_tweets = [tweet_info for tweet_info in sentiment_analysis_data if tweet_info['sentiment'] == 'negative']
        
        if (len(positive_tweets)/len(sentiment_analysis_data)) > \
            (len(negative_tweets)/len(sentiment_analysis_data)):
            return 'positive', positive_tweets, negative_tweets
        else:
            return 'negative', positive_tweets, negative_tweets
    
    def get_intensity_analyser_compound(self, tweet):
        analyser = SentimentIntensityAnalyzer()
        analysis = analyser.polarity_scores(tweet)
        if analysis['compound'] >= 0.05: 
            return 'positive' 
        elif analysis['compound'] <= -0.05: 
            return 'negative'
        else:
            return 'neutral'
            
    def prepare_intensity_sentiment_analysis(self, data):
        collection = []
        for tweet in data:
                parsed_data = {}
                clean_api = CleanTokens()
                cleaned_text = clean_api.clean_noise(tweet.get('text'))
                parsed_data['text'] = cleaned_text
                parsed_data['sentiment'] = self.get_intensity_analyser_compound(cleaned_text)
                if tweet.get('retweet_count') in tweet and tweet.get('retweet_count')> 0:
                    if parsed_data not in collection: 
                        collection.append(parsed_data) 
                else: 
                    collection.append(parsed_data)
        return collection
    
    def get_intensity_analyser(self, data):
        sentiment_analysis_data = self.prepare_intensity_sentiment_analysis(data)
        positive_tweets = [tweet_info for tweet_info in sentiment_analysis_data if tweet_info['sentiment'] == 'positive']
        negative_tweets = [tweet_info for tweet_info in sentiment_analysis_data if tweet_info['sentiment'] == 'negative']
        
        if (len(positive_tweets)/len(sentiment_analysis_data)) > \
            (len(negative_tweets)/len(sentiment_analysis_data)):
            return 'positive', positive_tweets, negative_tweets
        else:
            return 'negative', positive_tweets, negative_tweets