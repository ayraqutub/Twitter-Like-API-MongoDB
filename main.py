import json
import pymongo
from pymongo import MongoClient
import re
from datetime import datetime
import os
from load_json import*
from search_user_proj2 import*
from search_tweets import*
from top_users import*
from compose_tweets import *
from list_top_tweets import*

#json_name = input("name of json file : ")
while True:
        json_name = input("Enter the json file name: ")
        if os.path.exists(json_name):
            break
        else:
            print("Error: The specified file does not exist. Please enter a valid database file name.")
print(f"Using json file: {json_name}")
mongo_port = input("mongo port : ")
load_json(json_name, mongo_port)



while True:
        
        print("1. Search for Tweets")
        print("2. Search for Users")
        print("3. Compose a Tweet")
        print("4. List Tweets")
        print("5. List Users")
        print("6. exit")

        user_choice = input("Enter your choice: ")

        
        if user_choice == '1':
            search_tweets(mongo_port)
        elif user_choice == '2':
            search_users(mongo_port)
        elif user_choice == '3':
            tweet_text = input("Compose your tweet: ")
            compose_tweet(mongo_port, "user291", tweet_text)
        elif user_choice == '4':
            list_top_tweets(mongo_port)
        elif user_choice == '5':
            top_users(mongo_port)
        elif user_choice == '6':
            break
