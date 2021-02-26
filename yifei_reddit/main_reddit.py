from sentiment_anaylsis import SentimentAnaylsis
from api_reddit import APIReddit
def get_reddit_indicator(field):
    reddit = APIReddit()
    data = reddit.reddit_API(field)
    s = SentimentAnaylsis()
    return s.sentiment(data)

# if __name__ == "__main__":
#     get_reddit_indicator("apple")