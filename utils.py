import requests

def fetch_news(api_key, query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

def fetch_tweets(api_key, api_secret_key, access_token, access_token_secret, query):
    import tweepy
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search(q=query, lang="en", result_type="recent", count=100)
    return [tweet.text for tweet in tweets]
