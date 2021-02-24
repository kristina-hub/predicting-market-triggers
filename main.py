from kristina_global_news.main_global import MainGlobal
# from linna_stock_news.main_stock import MainStock
# from sadaf_twitter.main_twitter import MainTwitter
# from yifei_facebook.main_facebook import MainFacebook

class Main():

    if __name__ == "__main__":

        # return 1 if should buy stock
        # return 0 if should not buy stock

        result_1 = MainGlobal.run_global()
        # result_2 = MainStock.run_stock()
        # result_3 = MainTwitter.run_twitter()
        # result_4 = MainFacebook.run_facebook()

        result = result_1
        # result = (result_1 + result_2 + result_3 + result_4) / 4
        result = result * 100

        print("It is ", result, " % recommended that you buy this stock")
