import re
import unicodedata
from nltk.corpus import stopwords
import inflect
class CleanTokens(object):
    def clean_pattern(self, text, pattern):
        r = re.findall(pattern, text)
        for search_term in r:
            text = re.sub(search_term, '', text)        
        return text
    def clean_noise(self, text):
        remove_return_handler = self.clean_pattern(text, "RT @[\w]*:")
        remove_handler = self.clean_pattern(remove_return_handler, "@[\w]*")
        cleaned_text = self.clean_pattern(remove_handler, "https?://[A-Za-z0-9./]*")
        return cleaned_text
    def clean_non_ascii(self, list_of_tweets):
        normalized_list = []
        for txt in list_of_tweets:
            normalized_txt = unicodedata.normalize('NFKD', txt).encode(
                'ascii', 'ignore').decode('utf-8', 'ignore')
            normalized_list.append(normalized_txt)
        return normalized_list
    
    def lowercase(self,list_of_tweets):
        normalized_list = []
        for txt in list_of_tweets:
            normalized_txt = txt.lower()
            normalized_list.append(normalized_txt)
        return normalized_list
    
    def clean_punctuation(self,list_of_tweets):
        normalized_list = []
        for txt in list_of_tweets:
            normalized_txt = re.sub(r'[^\w\s]', '', txt)
            if normalized_txt != '':
                normalized_list.append(normalized_txt)
        return normalized_list
    
    def clean_numbers(self,list_of_tweets):
        ie = inflect.engine()
        normalized_list = []
        for txt in list_of_tweets:
            if txt.isdigit():
#                 print(txt)
                normalized_txt = ie.number_to_words(txt)
                normalized_list.append(normalized_txt)
            else:
                normalized_list.append(txt)
        return normalized_list
    
    def clean_stopwords(self,list_of_tweets):
        normalized_list = []
        for txt in list_of_tweets:
            if txt not in stopwords.words('english'):
                normalized_list.append(txt)
        return normalized_list
    
    def normalize_list_of_tweets(self, tweets):
#         print(len(tweets))
        normalized_list = self.clean_non_ascii(tweets)
        normalized_list = self.lowercase(normalized_list)
        normalized_list = self.clean_punctuation(normalized_list)
        normalized_list = self.clean_numbers(normalized_list)
        normalized_list = self.clean_stopwords(normalized_list)
        return normalized_list