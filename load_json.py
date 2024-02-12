import json
import pymongo
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor

def load_json(json_file, mongo_port):
    # Connect to MongoDB
    client = MongoClient(f"mongodb://localhost:{mongo_port}/")

    # Create or switch to the '291db' database
    db = client['291db']

    # Drop the 'tweets' collection if it exists
    db.drop_collection('tweets')

    # Create a new 'tweets' collection
    tweets_collection = db['tweets']

    # Define the number of threads (adjust based on your system)
    num_threads = 4

    # Read the JSON file and insert data into MongoDB in parallel batches
    with open(json_file, 'r', encoding='utf-8') as file:
        # Use ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            # Read lines from the file concurrently and insert batches
            for batch in json_file_batcher(file, batch_size=1000):
                executor.submit(insert_batch, tweets_collection, batch)

def json_file_batcher(file, batch_size):
    # Read the file in batches
    batch = []
    for line in file:
        tweet = json.loads(line)
        batch.append(tweet)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

def insert_batch(collection, batch):
    # Insert a batch of tweets into MongoDB
    collection.insert_many(batch)
