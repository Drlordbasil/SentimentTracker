import tweepy
from textblob import TextBlob
import time


class SentimentAnalyzer:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def fetch_tweets(self, topic):
        """
        Fetches real-time tweets based on the user-defined topic.
        """
        tweets = []
        try:
            for tweet in tweepy.Cursor(self.api.search, q=topic, tweet_mode='extended').items(100):
                tweets.append(tweet.full_text)
        except tweepy.TweepError as e:
            print(f"Error: {e}")
        return tweets

    @staticmethod
    def analyze_sentiment(text):
        """
        Applies sentiment analysis on the given text and returns the sentiment score.
        """
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def real_time_sentiment_analysis(self, topic):
        """
        Performs real-time sentiment analysis on social media posts related to the given topic.
        """
        print("Real-Time Social Media Sentiment Analyzer")
        print(f"Analyzing tweets related to '{topic}'...\n")

        while True:
            tweets = self.fetch_tweets(topic)
            for tweet in tweets:
                sentiment_score = self.analyze_sentiment(tweet)
                print(f"Tweet: {tweet}")
                print(f"Sentiment Score: {sentiment_score}")
                print("-" * 50)

            # Sleep for 1 minute before fetching tweets again
            time.sleep(60)


if __name__ == "__main__":
    # Enter your own Twitter API credentials
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    topic = input("Enter a topic or hashtag: ")

    sentiment_analyzer = SentimentAnalyzer(consumer_key, consumer_secret, access_token, access_token_secret)
    sentiment_analyzer.real_time_sentiment_analysis(topic)