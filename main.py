import re

input("Press ENTER if you have a 'tweets.py' file\n")

import tweets

clean_tweets = []
output_file1 = "tweets_by_line.txt"
output_file2 = "tweets.txt"

for rt in tweets.raw_tweets:
    cleaned_tweet = rt["tweet"]["full_text"]

    # Get rid of URLs for quoted tweets
    cleaned_tweet = re.sub("https:\/\/.*$", "", cleaned_tweet)

    # Get rid of @s
    cleaned_tweet = re.sub(r"(@\b.*?) ", "", cleaned_tweet)

    # Get rid of retweets
    cleaned_tweet = re.sub("RT.*", "", cleaned_tweet)

    # Replace HTML encodings with the characters
    cleaned_tweet = re.sub("&lt;", "<", cleaned_tweet)
    cleaned_tweet = re.sub("&gt;", ">", cleaned_tweet)
    cleaned_tweet = re.sub("&le;", "≤", cleaned_tweet)
    cleaned_tweet = re.sub("&ge;", "≥", cleaned_tweet)

    if cleaned_tweet.strip() == "" or cleaned_tweet.strip() == "\n":
        continue
    
    # Get rid of empty lines
    cleaned_tweet = re.sub("(?:[\t ]*(?:\r?\n|\r))+", ". ", cleaned_tweet)

    # Get rid of 
    
    clean_tweets.append(cleaned_tweet)

clean_tweets = list(set(clean_tweets)) # Remove duplicates

clean_tweets_2 = []
clean_tweets_3 = ""

for tweet in clean_tweets:
    # if len(tweet) <= 1:
    #     print(f"short: '{tweet}' | stripped: '{tweet.strip()}'")

    if tweet.strip() == "" or tweet.strip() == " ": # To stop empty lines
        continue
    
    # Else
    # f.write(f"{tweet.strip()}\n")
    clean_tweets_2.append(f"{tweet.strip()}\n")
    clean_tweets_3 += f"{tweet.strip()}. "

with open(output_file1, "a") as f:
    for tweet in clean_tweets_2:
        f.write(f"{tweet.strip()}\n")

with open(output_file2, "a") as f:
    f.write(clean_tweets_3.strip())