from api_facebook import FacebookAPI
from sentiment_anaylsis import SentimentAnaylsis

def get_facebook_indicator(keyword):
    facebook = FacebookAPI()
    data = facebook.get_data_from_group(keyword)
    if data:
        s = SentimentAnaylsis()
        indicator = s.sentiment(data)
    else:
        indicator = 0
    return indicator

