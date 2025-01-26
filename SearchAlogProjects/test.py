import json
import tweepy

br_token = 'AAAAAAAAAAAAAAAAAAAAAHiHsQEAAAAAmoEoEhkAo1JMSsL9DH7GIqlOyGM%3DqgJdWBh46iUvuWWb52c40TkKcTYR0FYqpQW3q2EhuJRvlFnCZ0'

def lambda_handler():
    # Set up Tweepy client with Bearer Token for API v2
    client = tweepy.Client(bearer_token=br_token)

    # Use the correct method for searching tweets in API v2
    try:
        query = 'Python'
        tweets = client.search_recent_tweets(query=query, max_results=5)

        tweet_list = [{"text": tweet.text, "user": tweet.author_id} for tweet in tweets.data]

        return {
            'statusCode': 200,
            'body': json.dumps(tweet_list)
        }
    except tweepy.TweepError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


result = lambda_handler()
print(result)
