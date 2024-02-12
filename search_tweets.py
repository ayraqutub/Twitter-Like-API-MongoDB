import pymongo
from pymongo import MongoClient
import re

def search_tweets(mongo_port):
    # Connect to MongoDB
    client = MongoClient(f"mongodb://localhost:{mongo_port}/")

    # Access the '291db' database and 'tweets2' collection
    db = client['291db']
    tweets_collection = db['tweets']
    
    # Check if the 'content_text' index exists before dropping
    existing_indexes = tweets_collection.index_information()
    if 'content_text' in existing_indexes:
        # Drop the existing index on 'content' field
        tweets_collection.drop_index('content_text')

    # Create a new index on the 'content' field for efficient keyword searches
    tweets_collection.create_index([('content', pymongo.TEXT)], name='content_text')


    while True:
        # Prompt user for keywords with error checks
        while True:
            user_keywords = input("Enter keywords (space-separated): ")
            
            if user_keywords.strip():  # Check if the input is not empty
                keywords = user_keywords.split()
                break
            else:
                print("Invalid input. Please enter at least one keyword.")

        # Search for tweets containing all entered keywords (unordered) with AND semantics
        query = {"$and": [{"content": {"$regex": f"\\b{re.escape(keyword)}\\b", "$options": "i"}} for keyword in keywords]}
        matching_tweets = list(tweets_collection.find(query))

        if not matching_tweets:
            print("No matching tweets found.")
        else:
            # Display relevant information for each matching tweet with a number
            for num, tweet in enumerate(matching_tweets, start=1):
                print(f"{num}. Tweet ID: {tweet['_id']}, Date: {tweet['date']}, Content: {tweet['content']}, Username: {tweet['user']['username']}")

            # Allow the user to select a tweet and view all fields
            while True:
                selected_tweet_id = input("Enter the number of the tweet you want to view (or 'exit' to end): ")

                if selected_tweet_id.lower() == 'exit':
                    break

                try:
                    selected_tweet_id = int(selected_tweet_id)
                    if 1 <= selected_tweet_id <= len(matching_tweets):
                        # Convert the user input to index
                        selected_tweet = matching_tweets[selected_tweet_id - 1]
                        # Display all fields of the selected tweet
                        print("\nSelected Tweet Fields:")
                        for field, value in selected_tweet.items():
                            print(f"\n{field}: {value}")
                        break
                    else:
                        print("Invalid tweet number. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        # Ask if the user wants to perform another search
        while True:
            another_search = input("Do you want to perform another search? (yes/no): ")

            if another_search.lower() == 'yes' or another_search.lower() == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if another_search.lower() != 'yes':
            break

    tweets_collection.drop_index('content_text')
