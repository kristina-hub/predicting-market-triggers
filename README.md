# Predicting-Market-Triggers
Build a product that focuses on predicting market-moving events before they become widely available on news sites (such as Thomson Reuters, Associate Press) that can be utilized by Citi market traders.

# kristina_global_news
User is prompted to input the name and category of the stock they want to purchase
An API gets the most recent news articles related to this stock
A classifier was trained with positive tweets and negative tweets to identify positive and negative words
The news articles are parsed into tokens and scanned for positive or negative connotations
If the majority of words relating to the stock are positive, the output suggests that the user buys the stock
If the majority of words relating to the stock are negative, the output suggests that the user should not buy the stock
