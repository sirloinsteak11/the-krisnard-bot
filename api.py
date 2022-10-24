import random
import tweepy as tw
from pygelbooru import Gelbooru
import os

blacklist = ['gore', 'rape', 'futa', 'loli', 'guro', 'snuff', 'amputation', 'pregnant']
 
# API keyws that yous saved earlier
bearer_token = os.environ['bearer_token']

# Authenticate to Twitter
tclient = tw.Client(bearer_token)

# gets specified user
user_id = os.environ['twit_user_id']

# hello gelbooru
gelbooru = Gelbooru()

#empty variables
tweet_list = []
tosendprevious = ''

async def get_random_tweet():
  response = tclient.get_liked_tweets(user_id, tweet_fields =["entities"], max_results=100)
  for tweet in response.data:
    tweets = tweet.id, tweet.entities
    tweet_list.append(tweets)
  liked_post = random.choice(tweet_list)
  first = liked_post[1]
  second = first.get('urls')
  third = second[0]
  return third.get('expanded_url')

async def get_random_gelbooru(tags):
  msgcontent = tags.replace('!gel', ' ')
  search2 = msgcontent.strip()
  results = await gelbooru.random_post(tags=search2, exclude_tags=blacklist)
  if not results:
    return 'no results found!!!'
  else:
    return results