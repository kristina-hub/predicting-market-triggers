from yifei_facebook.api_facebook import FacebookAPI
from yifei_facebook.sentiment_anaylsis import SentimentAnaylsis

class MainFacebook():

    def get_facebook_indicator(keyword):
        facebook = FacebookAPI()
        data = facebook.get_data_from_group(keyword)
        if data:
            s = SentimentAnaylsis()
            indicator = s.sentiment(data)
            print("Positive market triggers indicate that you should buy this stock")
        else:
            indicator = 0
            print("Negative market triggers indicate that you should not buy this stock")
        return indicator
