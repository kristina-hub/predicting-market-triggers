# Predicting-Market-Triggers

### Table of Contents
- [About](#About)
- [Examples of Use Cases](#Examples-of-Use-Cases)
- [Installation](#Installation)
- [Global News Kristina](#Global-News-Kristina)
- [Stock News Linna](#Stock-News-Linna)
- [Twitter Sadaf](#Twitter-Sadaf)
- [Facebook Yifei](#Facebook-Yifei)
- [Integration](#Integration)


## About
Build a product that focuses on predicting market-moving events before they become widely available on news sites (such as Thomson Reuters, Associate Press) that can be utilized by Citi market traders.

## Examples of Use Cases

1. Considers social media (e.g. Twitter, Facebook) and other types (e.g. Global News, Stock News)
2. Uses fast and slow media types to detect macro-trends so that we can assess the impact on various portfolios
3. Groups events in a trend based on how this will affect the markets and individual asset classes
4. Builds a product that could help us evaluate potential “macro trends” and their impact on stocks

## Installation

```shell script
$ pip install newsapi-python

```

## Global News Kristina
  - User is prompted to input the name and category of the stock they want to purchase
  - An API gets the most recent news articles related to this stock
  - A classifier was trained with positive tweets and negative tweets to identify positive and negative words
  - The news articles are parsed into tokens and scanned for positive or negative connotations
  - If the majority of words relating to the stock are positive, the output recommends to buy the stock
  - If the majority of words relating to the stock are negative, the output recommends to not buy the stock

### Training Classifier
  ![](kristina_global_news/demos/train_classifier_demo.gif)

### Future Improvements
  - Currently the classifier correctly identifies positive/negative syntax
  - Further improvement could be made, however, to catch certain semantics

### Positive Examples
  - "description": "The good news is the coronavirus that causes COVID-19 doesn't seem to mutate"
  - The classifier suggests to buy health stocks because the word "good" identifies this as a positive sentence
  - However, it is better to buy health stocks when coronavirus is spreading more, not less

### Negative Examples
  - "title": "Facebook Stock Is Being Hurt by Apple's Changes"
  - The classifier suggests to not buy apple stocks because the word "hurt" identifies this as a negative sentence
  - However, the negative word applies to facebook, not apple

### Demo
  ![](kristina_global_news/demos/global_news_demo.gif)

### Tools
  - Used NewsAPI https://newsapi.org/ because the free version allows 100 requests per day

## Stock News Linna
  - To do...

## Twitter Sadaf
  - To do...

## Facebook Yifei
  - To do...

## Integration
  - Each market trigger (Global/Stock News, Facebook, Twitter) returns 1 (buy) or 0 (don't buy)
  - The recommendation given (ex. 75% likely to be a good investment) is an average of all market triggers
  - Abstraction allows us to easily add more new market triggers in the future
