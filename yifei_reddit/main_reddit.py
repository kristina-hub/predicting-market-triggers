from yifei_reddit.sentiment_anaylsis import SentimentAnaylsis
from yifei_reddit.api_reddit import APIReddit
class MainReddit():
    def get_reddit_indicator(field):
        reddit = APIReddit()
        data = reddit.reddit_API(field)
        s = SentimentAnaylsis()
        return s.sentiment(data)

# if __name__ == "__main__":
#     get_reddit_indicator("apple")
