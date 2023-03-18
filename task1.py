import json
import glob

def task1():

    # Opens the file HealthStory.json and reads its data
    f = open('/course/data/a1/reviews/HealthStory.json')
    data = json.load(f)

    reviews = 0
    # Calculates each key of the dictionary within the json file as a review
    for individual_review in data:
        # Counts the total reviews by adding them up
        reviews += 1    

    # Calculates the total number of articles 
    # Coun the number of json files within the ../a1/content/HealthStory/ folder
    articles = len(glob.glob1('/course/data/a1/content/HealthStory/',"*.json"))

    # Opens the file containing the tweet IDs of tweets related to each article 
    fp = open('/course/data/a1/engagements/HealthStory.json')
    # Loads the data collected
    tweet_info = json.load(fp)

    # Calculates the total number of tweets
    all_tweets = []
    total_tweets = 0
    
    for article_no in tweet_info.keys():
        # Add all the tweet IDs of tweets, retweets, replies for each article to a list
        all_tweets.extend(tweet_info[article_no]['tweets'])
        all_tweets.extend(tweet_info[article_no]['retweets'])
        all_tweets.extend(tweet_info[article_no]['replies'])

    # Measure the length of the list to find the total number of unique tweets
    total_tweets = len(set(all_tweets))

    # Condense all the collected data in the form of a dictionary
    summary = {
        "Total number of articles": articles,
        "Total number of reviews": reviews,
        "Total number of tweets": total_tweets
    }

    # Appropriately format it and convert it into a json object
    json_object = json.dumps(summary, indent = 4)

    # Write the json object to a new json file as output
    with open("task1.json", "w") as outfile:
        outfile.write(json_object)
    return
