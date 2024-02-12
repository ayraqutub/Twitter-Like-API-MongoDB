import re
from datetime import datetime
import pymongo
from pymongo import MongoClient, ASCENDING

def compose_tweet(mongo_port, user_id, text):
    
    client = MongoClient(f"mongodb://localhost:{mongo_port}/")
    # Create or switch to the '291db' database
    db = client['291db']
    tweets_collection = db['tweets']

    # Get ID of new tweet
    tweet_id = get_unique_tweet_id(tweets_collection)

    # Construct tweet document
    tweet_data = {
    "url": f"https://twitter.com/{user_id}/status/{tweet_id}", #created by looking at the format of the provided tweets
    "date": datetime.now().strftime('%Y-%m-%d'),
    "content": text, 
    "renderedContent":None, 
    "id": None, 
    "user": {
        "username": "user291", 
        "displayname": None,
        "id": None, 
        "description": None, 
        "rawDescription": None, 
        "descriptionUrls": None, 
        "verified": None, 
        "created": None, 
        "followersCount": 0, 
        "friendsCount": 0, 
        "statusesCount":0, 
        "favouritesCount": 0, 
        "listedCount": 0, 
        "mediaCount": 0, 
        "location": None, 
        "protected": None, 
        "linkUrl": None, 
        "linkTcourl": None, 
        "profileImageUrl": None, 
        "profileBannerUrl": None, 
        "url": None
        }, 
    "outlinks": None, 
    "tcooutlinks": None, 
    "replyCount": 0, 
    "retweetCount": 0, 
    "likeCount": 0, 
    "quoteCount": 0, 
    "conversationId": None, 
    "lang": None, 
    "source": None, 
    "sourceUrl": None, 
    "sourceLabel": None, 
    "media": None, 
    "retweetedTweet": None, 
    "quotedTweet": None, 
    "mentionedUsers": None
    }

    # Set all other keys to None
    



    tweets_collection.insert_one(tweet_data)
    # Ensure an index on the 'url' field for faster searches
    # Check if the 'content' index exists before dropping
    existing_indexes = tweets_collection.index_information()
    if 'content_text' in existing_indexes:
        # Drop the existing index on 'content' field
        tweets_collection.drop_index('content_text')

    tweets_collection.create_index([("url", ASCENDING)])
    print("Successfully Tweeted")
    
def get_unique_tweet_id(collection):
    # Find the latest tweet and increment its id
    latest_tweet = collection.find_one(sort=[("url", -1)])
    if latest_tweet:
        return int(latest_tweet["url"].split("/")[-1]) + 1
    else:
        return 1
