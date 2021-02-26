import praw
import json
# MarketTriggerPredictor
# kZh9CJYRFIs-KiUx_itvV5p4ypdGyA

class APIReddit():
    def __init__(self):
        self.data = ""

    def reddit_API(self,field):
        reddit = praw.Reddit(client_id = "xEsubPACXyyESA",
                            client_secret = "kZh9CJYRFIs-KiUx_itvV5p4ypdGyA" ,
                            username = "PredictMarketTrigger",
                            password = "marketTrigger@CH",
                            user_agent = "market_trends")
        subreddit = reddit.subreddit(field)
        new_posts = subreddit.new()
        for sub in new_posts:
            if not sub.stickied:
                sub.comments.replace_more(limit=0)
                comments = sub.comments.list()
                for comment in sub.comments:
                    self.data = self.data + " " + comment.body
        return self.data

# if __name__ == "__main__":
#     r = APIReddit()
#     r.reddit_API("tesla")
