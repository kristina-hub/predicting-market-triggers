import random
import nltk
import pickle
from statistics import mode
from clean_tokens import CleanTokens
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.classify import ClassifierI
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC, NuSVC

class Train():

    def find_features(document, word_features):
        words = set(document)
        features = {}
        for w in word_features:
            features[w] = (w in words)
        return features


    def train(self):
        train_pos = open("./datasets/trainingData/positive.txt","r",encoding='latin-1').read()
        train_neg = open("./datasets/trainingData/negative.txt","r",encoding='latin-1').read()
        documents = []
        for r in train_pos.split('\n'):
            documents.append((r, "pos"))
        for r in train_neg.split('\n'):
            documents.append((r,"neg"))

        pickle_documents = open("algos_pickle/documents.pickle","wb")
        pickle.dump(documents, pickle_documents)
        pickle_documents.close()

        all_words = []
        train_clean_pos = CleanTokens.remove_noise(word_tokenize(train_pos))
        train_clean_neg = CleanTokens.remove_noise(word_tokenize(train_neg))
        for w in train_clean_pos:
            all_words.append(w.lower())
        for w in train_clean_neg:
            all_words.append(w.lower())
        all_words = nltk.FreqDist(all_words)
        word_features  = list(all_words.keys())[:5000]

        pickle_word_features = open("algos_pickle/word_features.pickle","wb")
        pickle.dump(word_features, pickle_word_features)
        pickle_word_features.close()

        feature_sets = [(Train.find_features(rev, word_features),category) for (rev, category) in documents]
        random.shuffle(feature_sets)
        training_set = feature_sets[:10000]
        testing_set = feature_sets[10000:]

        classifier = NaiveBayesClassifier.train(training_set)
        pickle_classifier = open("algos_pickle/naiveBayesC.pickle","wb")
        pickle.dump(classifier, pickle_classifier)
        pickle_classifier.close()

        MNB_classifier = SklearnClassifier(MultinomialNB())
        MNB_classifier.train(training_set)
        pickle_MNB = open("algos_pickle/MNB.pickle","wb")
        pickle.dump(MNB_classifier, pickle_MNB)
        pickle_MNB.close()

        BNB_classifier = SklearnClassifier(BernoulliNB())
        BNB_classifier.train(training_set)
        pickle_BNB = open("algos_pickle/BNB.pickle","wb")
        pickle.dump(BNB_classifier, pickle_BNB)
        pickle_BNB.close()

        LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        LogisticRegression_classifier.train(training_set)
        pickle_LogisticR = open("algos_pickle/LogisticR.pickle","wb")
        pickle.dump(LogisticRegression_classifier, pickle_LogisticR)
        pickle_LogisticR.close()

        SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
        SGDClassifier_classifier.train(training_set)
        pickle_SGDClassifier = open("algos_pickle/SGDClassifier.pickle","wb")
        pickle.dump(SGDClassifier_classifier, pickle_SGDClassifier)
        pickle_SGDClassifier.close()

        LinearSVC_classifier = SklearnClassifier(LinearSVC())
        LinearSVC_classifier.train(training_set)
        pickle_LinearSVC = open("algos_pickle/LinearSVC.pickle","wb")
        pickle.dump(LinearSVC_classifier, pickle_LinearSVC)
        pickle_LinearSVC.close()

        NuSVC_classifier = SklearnClassifier(NuSVC())
        NuSVC_classifier.train(training_set)
        pickle_NuSVC = open("algos_pickle/NuSVC.pickle","wb")
        pickle.dump(NuSVC_classifier, pickle_NuSVC)
        pickle_NuSVC.close()




# if __name__ == "__main__":
#     t = Train()
#     t.train()
    


