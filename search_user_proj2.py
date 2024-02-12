import json
import pymongo
from pymongo import MongoClient
import re

def search_users(mongo_port):
    # Connect to MongoDB
    client = MongoClient(f"mongodb://localhost:{mongo_port}/")
    db = client['291db']
    users_collection = db['tweets']  # Assuming users are stored in the 'tweets' collection

    # Create case-insensitive index for displayname and location fields
    users_collection.create_index([("user.displayname", pymongo.TEXT), ("user.location", pymongo.TEXT), ("user.followersCount", pymongo.DESCENDING)])

     # Use \b to match whole words in the regex
    keyword = input("Enter a keyword: ")
    regex = fr"\b{re.escape(keyword)}\b"
    query = {
        "$or": [
            {"user.displayname": {"$regex": regex, "$options": "i"}},
            {"user.location": {"$regex": regex, "$options": "i"}}
        ]
    }
    projection = {
        "user": 1,
    }

    # Add $sort stage to sort by followersCount in descending order
    result = users_collection.find(query)

    result_list = list(result)
    unique_user_ids = set()

    if not result_list:
        print("No users found with the specified keyword.")
        users_collection.drop_index([("user.displayname", pymongo.TEXT), ("user.location", pymongo.TEXT), ("user.followersCount", pymongo.DESCENDING)])
        return

    print("Users matching the keyword:")
    print("\n")
    num = 1
    i = 0
    no_dup_list = []
    for user in result_list :
        user_id = user['user']['username']

        if user_id not in unique_user_ids:
            unique_user_ids.add(user_id)
            print(f"{num}. Username: {user['user']['username']}, Display Name: {user['user']['displayname']}, Location: {user['user']['location']}")
            num += 1
            no_dup_list.append(result_list[i])
            i += 1
        else:
            i += 1
        
    # Allow the user to select a user
    while True:
        print("\n")
        selected_user_num = input("Enter the number of the user you want to view ('exit' to exit): ")

        if selected_user_num.isdigit() and 0 < int(selected_user_num) <= len(no_dup_list):
            selected_user = no_dup_list[int(selected_user_num) - 1]['user']

            print("\nSelected User Information:")
            for field, value in selected_user.items():
                print(f"\n{field}: {value}")
            break
        elif selected_user_num.lower() == 'exit':
            
            break
        else:
            print("Invalid selection. Please enter a valid user number or 'exit'.")
    users_collection.drop_index([("user.displayname", pymongo.TEXT), ("user.location", pymongo.TEXT), ("user.followersCount", pymongo.DESCENDING)])
