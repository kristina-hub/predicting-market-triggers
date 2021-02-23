import json

class SemanticAnalysis():

    def get_data():
        f = open('api_news.json',)
        data = json.load(f)

        for line in data['articles']:
            print(line['content'])

        f.close()
