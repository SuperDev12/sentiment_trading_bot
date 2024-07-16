import time
from utils import fetch_news, fetch_tweets
from sentiment_analysis import analyze_sentiment
from trading_bot import TradingBot

# API keys and other credentials
NEWS_API_KEY = 'your_news_api_key'
TWITTER_API_KEY = 'hRW3ZHchRO90O13SKOQqWeJn4'
TWITTER_API_SECRET_KEY = 'NL1WlSqYNa6iFAlfQEsym7wIkwrjisCToPpOtBH25hQnVM3DGQ'
TWITTER_ACCESS_TOKEN = '1020559238395879424-bw0kdsSIEF9UGlGXNhv5hNgPl2ZHyS'
TWITTER_ACCESS_TOKEN_SECRET = '37J0L53drlNecyHQ98MMIZSMjnIFIphSDK1keAJxavXNI'
UPSTOX_API_KEY = 'your_upstox_api_key'
UPSTOX_API_SECRET = 'your_upstox_api_secret'
UPSTOX_REDIRECT_URI = 'your_upstox_redirect_uri'
UPSTOX_ACCESS_TOKEN = 'your_upstox_access_token'

# Initialize trading bot
bot = TradingBot(api_key=UPSTOX_API_KEY, api_secret=UPSTOX_API_SECRET, redirect_uri=UPSTOX_REDIRECT_URI, access_token=UPSTOX_ACCESS_TOKEN)

def main():
    query = "reliance stock"
    news_data = fetch_news(NEWS_API_KEY, query)
    tweets = fetch_tweets(TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, query)

    sentiment_scores = []
    if news_data and 'articles' in news_data:
        for article in news_data['articles']:
            sentiment = analyze_sentiment(article['description'])
            sentiment_scores.append(sentiment)

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet)
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