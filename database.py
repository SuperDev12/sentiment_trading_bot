from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/tradingbot")
db = client.sentiment_trading_bot
collection = db.sentiment_data

def insert_sentiment(source, text, sentiment):
    sentiment_entry = {
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "source": source,
        "text": text,
        "sentiment": sentiment
    }
    collection.insert_one(sentiment_entry)

def fetch_historical_sentiment():
    return list(collection.find())

