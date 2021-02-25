from newsapi import NewsApiClient
import json

class API():

    def get_data(stock, category):
#         print("Categories: business, entertainment, health, science, sports, technology")
#         stock = input('Enter Stock: ') # apple, tesla etc...
#         category = input('Enter Category: ') # business, entertainment, health, science, sports, technology
#         print('Processing market triggers for ' + stock + ' of type ' + category)

        client = NewsApiClient(api_key='f88c6da0524b46d1bf259103a35b5282')

        query = client.get_top_headlines(q = stock,
                                         category = category,
                                         language = 'en',
                                         country = 'ca')

        with open('kristina_global_news/datasets/api_news.json', 'w', encoding='utf-8') as f:
            json.dump(query, f, ensure_ascii=False, indent=4)

        return query

    def output_json():
        query = get_data()

        with open('kristina_global_news/datasets/api_news.json', 'w', encoding='utf-8') as f:
            json.dump(query, f, ensure_ascii=False, indent=4)
