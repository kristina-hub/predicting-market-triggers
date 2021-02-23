from clean_tokens import CleanTokens
from nltk.corpus import twitter_samples, stopwords
from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import re, string, random

class TrainModel():

    def train_classifier():
        positive_tweets = twitter_samples.strings('positive_tweets.json')
        negative_tweets = twitter_samples.strings('negative_tweets.json')
        text = twitter_samples.strings('tweets.20150430-223406.json')
        tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

        stop_words = stopwords.words('english')
        positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
        negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

        positive_cleaned_tokens_list = []
        for tokens in positive_tweet_tokens:
            positive_cleaned_tokens_list.append(CleanTokens.remove_noise(tokens, stop_words))

        negative_cleaned_tokens_list = []
        for tokens in negative_tweet_tokens:
            negative_cleaned_tokens_list.append(CleanTokens.remove_noise(tokens, stop_words))

        all_pos_words = CleanTokens.get_all_words(positive_cleaned_tokens_list)
        freq_dist_pos = FreqDist(all_pos_words)
        print(freq_dist_pos.most_common(10))
        positive_tokens_for_model = CleanTokens.get_tweets_for_model(positive_cleaned_tokens_list)
        negative_tokens_for_model = CleanTokens.get_tweets_for_model(negative_cleaned_tokens_list)

        positive_dataset = [(tweet_dict, "Positive")
                             for tweet_dict in positive_tokens_for_model]

        negative_dataset = [(tweet_dict, "Negative")
                             for tweet_dict in negative_tokens_for_model]

        dataset = positive_dataset + negative_dataset
        random.shuffle(dataset)
        train_data = dataset[:7000]
        test_data = dataset[7000:]
        classifier = NaiveBayesClassifier.train(train_data)
        return classifier, test_data


    if __name__ == "__main__":
        classifier, test_data = train_classifier()
        print("Accuracy is:", classify.accuracy(classifier, test_data))
        print(classifier.show_most_informative_features(10))

        custom_tweet = "I ordered just once from TerribleCo, they screwed up, never used the app again."
        custom_tokens = CleanTokens.remove_noise(word_tokenize(custom_tweet))
        print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
