from facebook_scraper import get_posts
import json

class FacebookAPI:
    def __init__(self):
        self.data = ""
        self.groups = [2833245540101138,661139834555824,1351125638432100,232291238459595,225218582424235,323464318132136]

    print("Facebook API authenticated")
    def get_data_from_group(self,keyword):
        for group in self.groups:
            for post in get_posts(group=group):
                if post["text"]:
                    if keyword in post["text"]:
                        self.data = self.data + " " + post["text"]
        return self.data






# if __name__ == "__main__":
#     fb = FacebookAPI()
#     fb.get_data_from_group("OCGN Stock Forecast")
