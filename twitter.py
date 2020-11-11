import tweepy
import time
import secret

# Set Access to Twitter
auth = tweepy.OAuthHandler(secret.oauthKey, secret.oauthPass)
auth.set_access_token(secret.accessKey, secret.accessPass)

# Get API 
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Get my user
user = api.me()
# print(user.screen_name)

# for follower in tweepy.Cursor(api.followers).items():
    # print(follower.name)

# Search Term / Variables
search = '#100DaysOfCode'
nTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

