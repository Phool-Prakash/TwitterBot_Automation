import time
import tweepy

api_key = "IU3CjOYntdTCv6v6pAixEIkQv"
api_secret = "qdUkfVvbw2WY9bqxrCcRTOsLusW3J7hTg4JJXso3kfksOA7MZy"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAANK4rQEAAAAA8z4z8Z9zA7QO%2Fe0sUSgMOjIdF6I%3DEjYB9LpptMJQl6dEsGu6x6ayhATytw39CvyRPzU5iJ0pIuVV2s"
access_token = "1566771113304420353-UGeDfAiehbnFHPzgsvgYkEZsaCyIUU"
access_token_secret= "BauZWp2oTQyelrCOO7LkhWg82o9uZx8Gy7nMuDIwtJziS"

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api = tweepy.API(auth)


comments = [
    "Comment 1: #Article370 \n #Article370",
    # "Comment 2: Some other text",
    # "Comment 3: More comments",
    # Add more comments as needed
]

for i, comment in enumerate(comments, start=1):
    try:
        api.update_status(status=comment)
        print(f'Tweet #{i} posted successfully: {comment}')
    except Exception as e:
        print(f'Error posting tweet #{i}: {e}')

    # Add a delay if needed to avoid hitting rate limits
    time.sleep(5)
    
# this is for new tweet or new post 
# client.create_tweet(text = "#Uk07Rider")

# This is for like  (this is the tweet id: "1734144091800400012")
#  But now this wil not work because of Auth v2 (authentication)
# client.like("1734146119599595940") 

# For Retweet the Tweet (need Auth v2 and tweetId)
# client.retweet("1734146119599595940")

# For Reply under tweet (Auth v2 and tweetID and reply TweetText)
# client.create_tweet(in_reply_to_tweet_id='1734189722740895798',text='#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega\n#BabuBhaiyaJeetega')

#For Delete tweet
# client.delete_tweet("Tweet_id")

# Show tweets of your timeline

# for tweet in api.home_timeline():
#     print(tweet.text)

# Auth V2
# person = client.get_user(username= "narendramodi").data.id

# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)


