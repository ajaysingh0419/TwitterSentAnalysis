pip install tweepy textblob vaderSentiment wordcloud matplotlib
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Twitter API credentials (replace with your actual credentials)
API_KEY = 'your-api-key'
API_SECRET_KEY = 'your-api-secret-key'
ACCESS_TOKEN = 'your-access-token'
ACCESS_TOKEN_SECRET = 'your-access-token-secret'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define search term (related to 2024 Presidential Election)
search_term = "2024 Presidential Election"

# Number of tweets to fetch
tweet_count = 1000

# Fetch tweets
tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang="en", tweet_mode="extended").items(tweet_count)

# Extract tweet text
tweet_texts = [tweet.full_text for tweet in tweets]

# Sentiment analysis function
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Analyze sentiment for each tweet
sentiments = [get_sentiment(tweet) for tweet in tweet_texts]

# Show sentiment results (optional)
for tweet, sentiment in zip(tweet_texts[:5], sentiments[:5]):
    print(f"Tweet: {tweet}")
    print(f"Sentiment: {sentiment}\n")

# Create word cloud
all_tweets_text = ' '.join(tweet_texts)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_tweets_text)

# Display word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()
