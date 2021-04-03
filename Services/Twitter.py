import tweepy
import Keys

# Authenticate to Twitter
auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_TOKEN, Keys.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def auth():
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


def tweet(message: str) -> bool:
    try:
        status = api.update_status(message)
    except tweepy.error.TweepError:
        print("Error publishing tweet")
        return False

    test = status.__getattribute__("text")
    print(f'Tweet:\n"{test}"\npublished!')
    return True
