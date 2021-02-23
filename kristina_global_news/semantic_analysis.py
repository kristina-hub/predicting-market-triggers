import json

f = open('api_news.json',)
data = json.load(f)

for line in data['articles']:
    print(line['content'])

f.close()
