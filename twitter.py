import tweepy
from random import randint

# Authentication details. To  obtain these visit dev.twitter.com
CONSUMER_KEY = '4gMwcCMGagdcI9uQVPHE43g5f'
CONSUMER_SECRET = 'seRnttXROzQuHursY9t1XtYeX8aREupBlCGUhLBBOnLamD0eld'
ACCESS_KEY = '465525633-MbOOrGUs2kreXykPUOvITvWJ7atVzCZe01HQYMO8'
ACCESS_SECRET = 'bIEfL9rHzP1TiIsqSEvL1MdDj6thrDAXbOwcN8xvVqWBP'

# Connecting to twitter API using authentication details
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

usersList = ['','']
tweetsToTweet = ['','']


# This is the listener, responsible for receiving data
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status, count=1):

        # If the tweet comes from @__________
        if status.user.id_str == "000000000":  # check if actual author I'm trying to track
            print("@" + status.user.screen_name + ": " + status.text)
            api.update_status(
                "@" + status.user.screen_name + tweetsToTweet[randint(0,1)],
                in_reply_to_status_id=status.id)

    # If an error occurs, don't kill the stream and print the error code.
    def on_error(self, status_code):
        print(sys.stderr + ' Encountered error with status code: ' + status_code)
        return True

    # If a timeout occurs, don't kill the stream and display 'Timeout...'
    def on_timeout(self):
        print(sys.stderr + 'Timeout...')
        return True  # Don't kill the stream


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    print("Showing all new tweets from @_______:")
    streamApi = tweepy.streaming.Stream(auth, MyStreamListener())
    # Streaming tweets from a certain user (to get ID user getwitterid.com)
    streamApi.filter(follow=usersList, async=True)
