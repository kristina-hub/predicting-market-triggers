from newsapi import NewsApiClient # pip install newsapi-python
import json

class API():

    def get_data():
        stock = input('Enter stock: ') # apple, tesla etc...
        category = input('Enter category: ') # business, entertainment, health, science, sports, technology
        print('Processing score for ' + stock + ' of type ' + category)

        client = NewsApiClient(api_key='f88c6da0524b46d1bf259103a35b5282')

        query = client.get_top_headlines(q = stock,
                                         category = category,
                                         language = 'en',
                                         country = 'ca')
        return query

    def output_json():
        query = get_data()

        with open('api_news.json', 'w', encoding='utf-8') as f:
            json.dump(query, f, ensure_ascii=False, indent=4)
