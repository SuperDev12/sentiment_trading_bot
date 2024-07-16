import requests
import tweepy

def fetch_news(api_key, query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching news: {response.status_code}")
        return None

def fetch_tweets(api_key, api_secret_key, access_token, access_token_secret, query):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        tweets = api.search_tweets(q=query, lang="en", result_type="recent", count=100)
        return [tweet.text for tweet in tweets]
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []
