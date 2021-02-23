# Predicting-Market-Triggers

## Demo
![](pygooglenews-demo.gif)

### Table of Contents
- [About](#About)
- [Examples of Use Cases](#Examples-of-Use-Cases)
- [Installation](#Installation)
- [Global News Kristina](#Global-News-Kristina)
- [Stock News Linna](#Stock News-Linna)
- [Twitter Sadaf](#Twitter-Sadaf)
- [Facebook Yifei](#Facebook-Yifei)


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

### positive examples
  - "description": "The good news is the coronavirus that causes COVID-19 doesn't seem to mutate

### negative examples
  - "title": "Facebook Stock Is Being Hurt by Apple's Changes
  - "title": "Apple Beats Samsung For Top Smartphone Vendor Globally

## Stock News Linna
  - To do...

## Twitter Sadaf
  - To do...

## Facebook Yifei
  - To do...
