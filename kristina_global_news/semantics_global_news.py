import json

f = open('api_news.json',)
data = json.load(f)

for line in data['articles']:
    print(line['content'])

f.close()

# train with twitter dataset to recognize positive and negative stop_words
# give recent news articles to recognize if majority of articles are positive / negative
# if majority of articles are negative recommend not to buy stock
