from clean_tokens import CleanTokens
from train_model import TrainModel
from nltk.tokenize import word_tokenize
import json

class SemanticAnalysis():

    def get_data():
        f = open('api_news.json',)
        data = json.load(f)

        string = ""
        for line in data['articles']:
            if isinstance(line['content'], str):
                string = string + " " + line['content']

        f.close()
        return string

    if __name__ == "__main__":
        news_content = get_data()
        classifier, test_data, freq_dist_pos = TrainModel.train_classifier()
        custom_tokens = CleanTokens.remove_noise(word_tokenize(news_content))

        print("Should I buy this stock?")
        print(classifier.classify(dict([token, True] for token in custom_tokens)))
