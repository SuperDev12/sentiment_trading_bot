import requests
import praw

def fetch_news(api_key, query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching news: {response.status_code}")
        return None

def fetch_reddit_posts(client_id, client_secret, user_agent, query):
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    subreddit = reddit.subreddit("all")
    posts = []
    for submission in subreddit.search(query, limit=100):
        posts.append(submission.title + " " + submission.selftext)
    return posts
