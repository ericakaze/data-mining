#create virtual environment
#activate it 
# pip install tweepy
import keys
import tweepy

auth= tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API (auth, wait_on_rate_limit= True, wait_on_rate_limit_notify=True)

user= api.get_user('ericakaze') 

#print(user.name)

#print(user.description)

#print(user.status.text)

#print(user.followers_count)

#print(user.friends_count)

me= api.me()

#print(me)


followers = []
### this is a list 
cursor = tweepy.Cursor (api.followers, screen_name='ericakaze')
### this will give us info about followers about followers of Nasa but we can only evaluate 10 at a time due to Twitter restrictions 

for account in cursor.items(10):
    followers.append(account.screen_name)

print(followers)
### about to use join function like sql 
print('followers:', ' '.join(sorted(followers, key=lambda s: s.lower())))

### we are sorting the followers
### we want the lowercase

friends= []

print('friends:', ' '.join(sorted(friends, key=lambda s: s.lower())))

tweets=api.user_timeline(screen_name='ericakaze', count=3)
### this is to get the last three tweets 

for tweet in tweets:
    print(tweet.text, '\n')