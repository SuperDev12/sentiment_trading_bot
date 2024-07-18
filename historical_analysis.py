import matplotlib.pyplot as plt
from database import fetch_historical_sentiment

def analyze_historical_sentiment():
    data = fetch_historical_sentiment()
    dates = [entry['date'] for entry in data]
    sentiments = [entry['sentiment'] for entry in data]

    plt.plot(dates, sentiments)
    plt.xlabel('Date')
    plt.ylabel('Sentiment')
    plt.title('Historical Sentiment Analysis')
    plt.show()

if __name__ == "__main__":
    analyze_historical_sentiment()
