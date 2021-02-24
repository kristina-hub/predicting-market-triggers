from kristina_global_news.main import Main as global
from linna_stock_news.main import Main as stock
from sadaf_twitter.main import Main as twitter
from yifei_facebook.main import Main as facebook

class Main():

    if __name__ == "__main__":

        # return 1 if should buy stock
        # return 0 if should not buy stock
        result_1 = global()
        result_2 = stock()
        result_3 = twitter()
        result_4 = facebook()

        result = (result_1 + result_2 + result_3 + result_4) / 4
        result = result * 100

        print("It is ", result, " % recommended that you buy this stock")
