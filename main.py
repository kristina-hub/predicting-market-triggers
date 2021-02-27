from flask import Flask, render_template, request, jsonify, abort
from kristina_global_news.main_global import MainGlobal
from sadaf_twitter.main_twitter import MainTwitter
from yifei_facebook.main_facebook import MainFacebook
from yifei_reddit.main_reddit import MainReddit
import os
app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")
@app.route("/")
def home():
    return render_template("index.html", Categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology'])

@app.route("/readme/")
def readme():
    return render_template("readme.html")
@app.route("/search",methods=["POST"])
def search():
#     print('Enter Stock name')
    try:
        stock = request.get_json().get('stock',None)
        category = request.get_json().get('category',None)
        print(stock, category)
        mainTwitter = MainTwitter()
        result_twitter = mainTwitter.run(stock)
        result_global = MainGlobal.run_global(stock,category)
        result_facebook = MainFacebook.get_facebook_indicator(stock)
        result_reddit = MainReddit.get_reddit_indicator(stock)
        return jsonify(status=[result_twitter, result_global, result_facebook, result_reddit])
    except Exception as e:
            abort(e.code, str(e))

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
