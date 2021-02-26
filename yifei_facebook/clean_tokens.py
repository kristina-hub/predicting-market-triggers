import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


class CleanTokens():

    def remove_noise(tokenized):
        filtered = []
        lemmatizer = WordNetLemmatizer()
        for token, tagged in nltk.pos_tag(tokenized):
            token = re.sub(r'http?://\S+','', token)
            token = re.sub(r'@\S+', '', token)
            token  = re.sub(r'[^\w\s]','',token)
            token = lemmatizer.lemmatize(token)
            if len(token) != 0 and token.lower() not in stopwords.words('english') and tagged.startswith("J"):
                filtered.append(token.lower())
        return filtered

# if __name__ == "__main__":
#     cl = CleanTokens()
#     text="I am really Happy tody, a @book is super better, my friend cheated on me, check this link below!!!!!https://dsjfhdsjhfds.com and this http://sdkjhfjksdhf "
#     filtered = cl.remove_noise(word_tokenize(text))
#     print(filtered)



