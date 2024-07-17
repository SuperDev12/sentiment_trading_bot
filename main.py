import time
from utils import fetch_news, fetch_reddit_posts
from sentiment_analysis import analyze_sentiment
from trading_bot import TradingBot

# API keys and other credentials
NEWS_API_KEY = '082ff6e130fc4ecb84efd99c0f6d70bc'
REDDIT_CLIENT_ID = 'NuptsGvBxq8hQXV0aDdoSA'
REDDIT_CLIENT_SECRET = 'migENcjbz2UhRBLArL04p4fA6UN5mQ'
REDDIT_USER_AGENT = 'python:sentiment_tradingbot:v1.0 (by /u/super-bakchod)'
UPSTOX_API_KEY = 'cbc66185-898f-4059-9333-1df4dd33d767'
UPSTOX_API_SECRET = 'xhat00t1rg'
UPSTOX_REDIRECT_URI = 'http://localhost:8000/callback' 
UPSTOX_ACCESS_TOKEN = 'your_upstox_access_token'
# Initialize trading bot
bot = TradingBot(api_key=UPSTOX_API_KEY, api_secret=UPSTOX_API_SECRET, redirect_uri=UPSTOX_REDIRECT_URI, access_token=UPSTOX_ACCESS_TOKEN)

def main():
    query = "reliance stock"
    news_data = fetch_news(NEWS_API_KEY, query)
    reddit_posts = fetch_reddit_posts(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, query)

    sentiment_scores = []
    if news_data and 'articles' in news_data:
        for article in news_data['articles']:
            sentiment = analyze_sentiment(article['description'])
            sentiment_scores.append(sentiment)

    for post in reddit_posts:
        sentiment = analyze_sentiment(post)
        sentiment_scores.append(sentiment)

    if sentiment_scores:
        average_sentiment = sum(sentiment_scores) / len(sentiment_scores)

        if average_sentiment > 0:
            order_id = bot.place_order("RELIANCE", "BUY", 1)
            if order_id:
                bot.modify_order(order_id, quantity=2)
                bot.cancel_order(order_id)
        else:
            order_id = bot.place_order("RELIANCE", "SELL", 1)
            if order_id:
                bot.modify_order(order_id, quantity=2)
                bot.cancel_order(order_id)

        order_details = bot.get_order_details(order_id)
        order_history = bot.get_order_history()
        order_book = bot.get_order_book()
        trades = bot.get_trades()
        order_trades = bot.get_order_trades(order_id)
        trade_history = bot.get_trade_history()

        print("Order Details:", order_details)
        print("Order History:", order_history)
        print("Order Book:", order_book)
        print("Trades:", trades)
        print("Order Trades:", order_trades)
        print("Trade History:", trade_history)
    else:
        print("No sentiment scores to process.")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)  # Run every hour