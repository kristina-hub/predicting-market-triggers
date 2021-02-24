from kristina_global_news.clean_tokens import CleanTokens
from nltk.corpus import twitter_samples, stopwords
from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import re, string, random

class TrainModel():

    def train_classifier():
        stop_words = stopwords.words('english')
        positive_tokens = twitter_samples.tokenized('positive_tweets.json')
        negative_tokens = twitter_samples.tokenized('negative_tweets.json')

        positive_cleaned_tokens = []
        for tokens in positive_tokens:
            positive_cleaned_tokens.append(CleanTokens.remove_noise(tokens, stop_words))

        negative_cleaned_tokens = []
        for tokens in negative_tokens:
            negative_cleaned_tokens.append(CleanTokens.remove_noise(tokens, stop_words))

        all_pos_words = CleanTokens.get_words(positive_cleaned_tokens)
        all_neg_words = CleanTokens.get_words(negative_cleaned_tokens)
        freq_dist_pos = FreqDist(all_pos_words)
        freq_dist_neg = FreqDist(all_neg_words)

        positive_tokens_for_model = CleanTokens.get_dict(positive_cleaned_tokens)
        positive_dataset = [(tweet_dict, "Positive")
                             for tweet_dict in positive_tokens_for_model]

        negative_tokens_for_model = CleanTokens.get_dict(negative_cleaned_tokens)
        negative_dataset = [(tweet_dict, "Negative")
                             for tweet_dict in negative_tokens_for_model]

        dataset = positive_dataset + negative_dataset
        random.shuffle(dataset)
        train_data = dataset[:7000]
        test_data = dataset[7000:]
        #print(test_data)
        classifier = NaiveBayesClassifier.train(train_data)
        return classifier, test_data, freq_dist_pos, freq_dist_neg
