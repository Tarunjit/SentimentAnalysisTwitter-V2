import twitter
import json

CONSUMER_KEY = "vVypmaitmk21exXEo22Bi691H"
CONSUMER_SECRET = "9wWmNH6UgDafRuZKTZ02G7arEf9YsJfH2oYanaE6itk0FyMFKA"
OAUTH_TOKEN = "91070076-hXHCPWZNQiJ1LwwUFZLzjGJXMZLwoJkbZLKVCi6jx"
OAUTH_TOKEN_SECRET = "V0zScYzfuKBTl0VWWHpG84Y34gNGkIN80PDs5eQsnEdgO"


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = 'microsoft'

count = 100

search_results = twitter_api.search.tweets(q=q, count=count)

print search_results