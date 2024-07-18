import requests
import praw

def fetch_news(api_key, query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

def fetch_reddit_posts(client_id, client_secret, user_agent, query):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    subreddit = reddit.subreddit("all")
    posts = []
    for submission in subreddit.search(query, limit=10):
        posts.append(submission.title + " " + submission.selftext)
    return posts
