from pymongo import MongoClient

def list_top_tweets(mongo_port):
    # Connect to MongoDB
    client = MongoClient(f"mongodb://localhost:{mongo_port}/")

    # Switch to the '291db' database
    db = client['291db']

    # Get the 'tweets' collection
    tweets_collection = db['tweets']

    #index 
    
    tweets_collection.create_index([('retweetCount', -1)])
    tweets_collection.create_index([('likeCount', -1)])
    tweets_collection.create_index([('quoteCount', -1)])
    
    # Get user input for sorting and limiting
    fields = ["retweetCount", "likeCount", "quoteCount"]

    # receive user input for one of retweetCount, likeCount, quoteCount
    while True:
        field = input("Enter the field to sort by (retweetCount, likeCount, quoteCount): ")
        if field in fields:
            break
        else:
            print("Invalid input. Please enter a valid field.")

    #receive user input for n (top n tweets)
    while True:
        n = input("Enter the number of top tweets to display: ")
        if n.isdigit():
            break
        else:
            print("Invalid input. Please enter a valid number.")

    # Find top n tweets based on field in descending order (limited to how many the user wants)
    top_tweets = list(tweets_collection.find().sort([(field, -1)]).limit(int(n)))

    # Display information for each matching tweet
    for index, tweet in enumerate(top_tweets, start=1):
        print("\n")
        print(f"{index}. Tweet ID: {tweet['_id']}")
        print(f"Date: {tweet['date']}")
        print(f"Content: {tweet['content']}")
        print(f"Username: {tweet['user']['username']}")
        # not required but for checking correctness, diplay inidcated field and number
        print(f"{field}: {tweet[field]}")
        print("\n")


    
    # select for more information
    # adapted from search for users to mathc usability 
    valid = False
    while valid == False:
            print("\n")
            selected_index= (input("Enter the number of the tweet you want to view ('exit' to exit): "))
            
            # ensure valid input
            if selected_index.isdigit():
                if 0 < int(selected_index) <= len(top_tweets):
                    selected_tweet = top_tweets[int(selected_index) - 1]

                    # print all fields
                    for field, value in selected_tweet.items():
                         print(f"\n{field}: {value}")
                else:
                    print("Invalid selection. Please enter a valid tweet number.")
            elif selected_index == 'exit':
                valid = True
            else :
                print("Invalid selection. Please enter a valid tweet number.")
