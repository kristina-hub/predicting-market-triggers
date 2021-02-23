from clean_tokens import CleanTokens
from api_news import API
from train_model import TrainModel
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import json

class Main():

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

        # print("Accuracy is:", classify.accuracy(classifier, test_data))
        # print(freq_dist_pos.most_common(10))
        # print(classifier.show_most_informative_features(10))
