from kristina_global_news.clean_tokens import CleanTokens
from kristina_global_news.api_news import API
from kristina_global_news.train_model import TrainModel
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import json
import time

class MainGlobal():

    def use_json():
        f = open('api_news.json',)
        data = json.load(f)

        string = ""
        for line in data['articles']:
            if isinstance(line['content'], str):
                string = string + " " + line['content']

        f.close()
        return string

    def use_api():
        data = API.get_data()
        string = ""
        for line in data['articles']:
            if isinstance(line['content'], str):
                string = string + " " + line['content']
        return string

    def run_global():
        news_content = MainGlobal.use_api()
        #news_content = use_json()
        #news_content = "I ordered just once from TerribleCo, they screwed up, never used the app again."

        classifier, test_data, freq_dist_pos, freq_dist_neg = TrainModel.train_classifier()
        custom_tokens = CleanTokens.remove_noise(word_tokenize(news_content))
        indication = classifier.classify(dict([token, True] for token in custom_tokens))

        if (indication == "Positive"):
            print(indication, " market triggers indicate that you should buy this stock")
            return 1;
        else:
            print(indication, " market triggers indicate that you should not buy this stock")
            return 0;


    if __name__ == "__main__":

        news_content = use_api()
        #news_content = use_json()
        #news_content = "I ordered just once from TerribleCo, they screwed up, never used the app again."

        classifier, test_data, freq_dist_pos, freq_dist_neg = TrainModel.train_classifier()
        custom_tokens = CleanTokens.remove_noise(word_tokenize(news_content))
        indication = classifier.classify(dict([token, True] for token in custom_tokens))

        if (indication == "Positive"):
            print(indication, " market triggers indicate that you should buy this stock")
        else:
            print(indication, " market triggers indicate that you should not buy this stock")

        # print()
        # print("Training Classifier")
        # classifier, test_data, freq_dist_pos, freq_dist_neg = TrainModel.train_classifier()
        # print("Accuracy is:", classify.accuracy(classifier, test_data))
        # print("Positive tokens: ", freq_dist_pos.most_common(10))
        # print("Negative tokens: ", freq_dist_neg.most_common(10))
        # print()
        # time.sleep(5)
        # print(classifier.show_most_informative_features(10))
        #
        # print("Testing Classifier")
        # print()
        # time.sleep(5)
        #
        # news_content = "I ordered just once from TerribleCo, they screwed up, never used the app again."
        # print(news_content)
        # custom_tokens = CleanTokens.remove_noise(word_tokenize(news_content))
        # indication = classifier.classify(dict([token, True] for token in custom_tokens))
        # print(indication, " sentence")
        # print()
        # time.sleep(5)
        #
        # news_content = "I love playing tennis, I enjoy going for walks and my favourite food is pizza."
        # print(news_content)
        # custom_tokens = CleanTokens.remove_noise(word_tokenize(news_content))
        # indication = classifier.classify(dict([token, True] for token in custom_tokens))
        # print(indication, " sentence")
        # print()
