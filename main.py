import time
from utils import fetch_news, fetch_reddit_posts, fetch_market_data
from sentiment_analysis import analyze_sentiment
from trading_bot import TradingBot
from database import insert_sentiment, fetch_historical_sentiment

# API keys and other credentials
NEWS_API_KEY = '082ff6e130fc4ecb84efd99c0f6d70bc'
REDDIT_CLIENT_ID = 'NuptsGvBxq8hQXV0aDdoSA'
REDDIT_CLIENT_SECRET = 'migENcjbz2UhRBLArL04p4fA6UN5mQ'
REDDIT_USER_AGENT = 'python:sentiment_tradingbot:v1.0 (by /u/super-bakchod)'
ALPHA_VANTAGE_API_KEY = 'QJUPAU6QRD2ZSL0F'

# Initialize trading bot
bot = TradingBot(api_key=ALPHA_VANTAGE_API_KEY)

def main():
    query = "reliance stock"
    news_data = fetch_news(NEWS_API_KEY, query)
    reddit_posts = fetch_reddit_posts(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, query)

    sentiment_scores = []
    if news_data and 'articles' in news_data:
        for article in news_data['articles']:
            sentiment = analyze_sentiment(article['description'])
            sentiment_scores.append(sentiment)
            insert_sentiment('news', article['description'], sentiment)

    for post in reddit_posts:
        sentiment = analyze_sentiment(post)
        sentiment_scores.append(sentiment)
        insert_sentiment('reddit', post, sentiment)

    historical_sentiment = fetch_historical_sentiment()
    print("Historical Sentiment Data:", historical_sentiment)

    if sentiment_scores:
        average_sentiment = sum(sentiment_scores) / len(sentiment_scores)

        # Fetch market data from Alpha Vantage
        symbol = "RELIANCE.BSE"
        market_data = fetch_market_data(ALPHA_VANTAGE_API_KEY, symbol)
        print(market_data)

        stop_loss = 2000  # Example value
        take_profit = 2200  # Example value

        if average_sentiment > 0:
            order_id = bot.place_order(symbol, "BUY", 1, stop_loss, take_profit)
            if order_id:
                bot.modify_order(order_id, quantity=2)
                bot.cancel_order(order_id)
        else:
            order_id = bot.place_order(symbol, "SELL", 1, stop_loss, take_profit)
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