__author__ = "Sadaf Najam"
__version__ = "1.0.0"
__email__ = "sadaf.najam91@gmail.com"
__status__ = "development"


from nltk.sentiment import SentimentIntensityAnalyzer
import re
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
from src.CSVWriterModule.CSVWriterModule import CsvWriter

sentiment_analyzer = SentimentIntensityAnalyzer()

def remove_url(txt):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    no_url = url_pattern.sub(r'', txt)
    return no_url


def _get_status_row(status):
    if 'retweeted_status' in status._json:
        full_text = status.retweeted_status.text
    else:
        full_text = status.text

    score = sentiment_analyzer.polarity_scores(full_text)

    return [
               status.created_at,
               full_text,
               status.user.followers_count
           ] + list(score.values())
           
from src.TwitterModule.twitter_module import TwitterData
if __name__ == "__main__":
    twitter_data = TwitterData(
    'vKw3DGGkKEKx9is4d11zRzm2n',
    'kvBll57qOpzyS7ryIGNGg74llQrHJEhoHBL940iEwHPKdLSJKg',
    '860140613467033600-9ZQyZCunQ3z0USEl03ASx7qkMGfL4u9',
    'LMeUgg71nMUSFJStzaNMPV2bTPbgEFDkzWd9ORlDSAQQ3')
    query = '#Microsoft'
    new_search = query + "-filter:retweets"
    tweets = twitter_data.search(new_search,1000)
#     for tweet in tweets:
#         print(tweet)
#     tweets_no_urls = [remove_url(tweet.text) for tweet in tweets]
    csv_header = ['Date', 'Content', 'Followers', 'Negative Score', 'Neutral Score', 'Positive Score',
                           'Compound Score']
    csv_writer = CsvWriter(
    './data',
    f'tweets_{query}.csv')
    csv_writer.add_row(csv_header)
    for status in tweets:
#         print(status)
        status = _get_status_row(status)
#         print(status)
#         if query not in status[1].lower():
#             continue
        csv_writer.add_row(status)
#         print(status)
    print('Completed CSV writing')
#     print(tweets_no_urls[:5])
#     sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]
#     sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]
#     sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])
#     sentiment_df = sentiment_df[sentiment_df.polarity != 0]
#     print(sentiment_df.head())
#     
#     fig, ax = plt.subplots(figsize=(8, 6))
#     sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
#                  ax=ax,
#                  color="purple")
#     
#     plt.title("Sentiments from Tweets on Market Movements")
#     plt.show()
#     for tweet in tweets:
#         print([tweet.user.screen_name.encode("utf-8"), tweet.user.location.encode("utf-8")])