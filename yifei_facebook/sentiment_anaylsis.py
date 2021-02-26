import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
from train_model import Train


class OptimalClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers


    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)


class SentimentAnaylsis(): 
    def load_all_classifiers(self):
        c_file = open("algos_pickle/naiveBayesC.pickle","rb")
        self.classifier = pickle.load(c_file)
        c_file.close()

        c_file = open("algos_pickle/MNB.pickle","rb")
        self.MNB_classifier = pickle.load(c_file)
        c_file.close()

        c_file = open("algos_pickle/BNB.pickle","rb")
        self.BNB_classifier = pickle.load(c_file)
        c_file.close()

        c_file = open("algos_pickle/LogisticR.pickle","rb")
        self.LogisticR = pickle.load(c_file)
        c_file.close()

        c_file = open("algos_pickle/SGDClassifier.pickle","rb")
        self.SGDC_classifier = pickle.load(c_file)
        c_file.close()

        c_file = open("algos_pickle/LinearSVC.pickle","rb")
        self.LinearSVC_classifier = pickle.load(c_file)
        c_file.close()

        c_file = open("algos_pickle/NuSVC.pickle","rb")
        self.NuSVC_classifier = pickle.load(c_file)
        c_file.close()
    
    
    def sentiment(self,data):
        word_feature_file = open("algos_pickle/word_features.pickle","rb")
        word_feature = pickle.load(word_feature_file)
        word_feature_file.close()
        SentimentAnaylsis.load_all_classifiers(self)
        optimal = OptimalClassifier(self.classifier,
                                    self.MNB_classifier,
                                    self.BNB_classifier,
                                    self.LogisticR,
                                    self.SGDC_classifier,
                                    self.LinearSVC_classifier,
                                    self.NuSVC_classifier)
        f = Train.find_features(data, word_feature)
        indicator = optimal.classify(f)
        if indicator == "pos":
            result = 1
        else:
            result = 0
        return result

# if __name__ == "__main__":
#     s =SentimentAnaylsis();
#     print(s.sentiment("and there were pythons...so yea! This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
#     print(s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))



        