from pymongo import MongoClient, DESCENDING, ASCENDING
def top_users(mongo_port):
    # Connect to MongoDB
    client = MongoClient(f"mongodb://localhost:{mongo_port}/")

    # Switch to the '291db' database
    db = client['291db']
    
    # Get the 'tweets' collection
    tweets_collection = db['tweets']
    tweets_collection.create_index([('user.followersCount', DESCENDING)])
    tweets_collection.create_index([('user.username', ASCENDING)])
    
    while True:
        n = input("Enter the number of users to display: ")
        if n.isdigit():
            break
        else:
            print("Invalid input. Please enter a valid digit.")


    #create dictionary to update users follwing count based on the max number of followers they have
    max_follower_count = {}

    # Fetch top users without duplicates
    top_users = []
    for user in tweets_collection.find().sort([('user.followersCount', -1)]):
        username = user['user']['username']
        followers_count = user['user']['followersCount']

        # Update the maximum followersCount for the user
        if username not in max_follower_count or followers_count > max_follower_count[username]:
            max_follower_count[username] = followers_count

            # Keep track of unique usernames
            top_users.append(user)

        # Break when the desired number of top users is reached
        if len(top_users) == int(n):
            break
        
    for index, user in enumerate(top_users, start=1):
        print("\n")
        print(f"{index}. Username: {user['user']['username']}")
        print(f"Display Name: {user['user']['displayname']}")
        #display the max follwer count for that user
        print(f"Followers Count: {max_follower_count[user['user']['username']]}")
        print("\n")

    # Get user input to select a user for more information
    valid = False
    while valid == False:
            print("\n")
            selected_index= (input("Enter the number of the user you want to view ('exit' to exit): "))
            
            # ensure input is valid digit 
            if selected_index.isdigit():
                if 0 < int(selected_index) <= len(top_users):
                    selected_user = top_users[int(selected_index) - 1]
                
                    # print all user fields
                    for field, value in selected_user['user'].items():
                        print(f"\n {field}: {value}")
                else:
                    print("Invalid selection. Please enter a valid user number.")
            elif selected_index == 'exit':
                valid = True
            else :
                print("Invalid selection. Please enter a valid user number.")
