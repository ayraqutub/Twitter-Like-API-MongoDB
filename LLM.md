# More detail of any AI tool used, including the name, URL, all the input given and all the output received.  
Case 1
Used Chatgpt (https://chat.openai.com/) and asked for the keys from the json schema to be extracted and placed into an array 

Input: 
Extract keys and place in array
``` {"url": "https://twitter.com/Davidmu66668113/status/1376738579171344386", "date": "2021-03-30T03:30:30+00:00", "content": "You hate farmers I hate you, \nif you love them I love you! ;) \n\n#StopHateAgainstFarmers \n#FarmersProtest", "renderedContent": "You hate farmers I hate you, \nif you love them I love you! ;) \n\n#StopHateAgainstFarmers \n#FarmersProtest", "id": 1376738579171344386, "user": {"username": "Davidmu66668113", "displayname": "tera jija \ud83e\udd28\ud83d\udea9\ud83c\uddfa\ud83c\uddf8", "id": 1357311756532649985, "description": "dream boy \ud83c\udf2a\ud83c\udf0d\ud83d\udd25\ud83d\udcaf", "rawDescription": "dream boy \ud83c\udf2a\ud83c\udf0d\ud83d\udd25\ud83d\udcaf", "descriptionUrls": [], "verified": false, "created": "2021-02-04T12:55:36+00:00", "followersCount": 18, "friendsCount": 286, "statusesCount": 347, "favouritesCount": 520, "listedCount": 0, "mediaCount": 3, "location": "", "protected": false, "linkUrl": null, "linkTcourl": null, "profileImageUrl": "https://pbs.twimg.com/profile_images/1376007034341007364/axPJoIKa_normal.jpg", "profileBannerUrl": "https://pbs.twimg.com/profile_banners/1357311756532649985/1616836224", "url": "https://twitter.com/Davidmu66668113"}, "outlinks": [], "tcooutlinks": [], "replyCount": 0, "retweetCount": 0, "likeCount": 1, "quoteCount": 0, "conversationId": 1376738579171344386, "lang": "en", "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", "sourceUrl": "http://twitter.com/download/android", "sourceLabel": "Twitter for Android", "media": null, "retweetedTweet": null, "quotedTweet": null, "mentionedUsers": null}```
Output:
   ``` json_keys = [
    "url",
    "date",
    "content",
    "renderedContent",
    "id",
    "user",
    "username",
    "displayname",
    "id",
    "description",
    "rawDescription",
    "descriptionUrls",
    "verified",
    "created",
    "followersCount",
    "friendsCount",
    "statusesCount",
    "favouritesCount",
    "listedCount",
    "mediaCount",
    "location",
    "protected",
    "linkUrl",
    "linkTcourl",
    "profileImageUrl",
    "profileBannerUrl",
    "url",
    "outlinks",
    "tcooutlinks",
    "replyCount",
    "retweetCount",
    "likeCount",
    "quoteCount",
    "conversationId",
    "lang",
    "source",
    "sourceUrl",
    "sourceLabel",
    "media",
    "retweetedTweet",
    "quotedTweet",
    "mentionedUsers"
]
```
We then used this to update null fields in compose_tweets. 

