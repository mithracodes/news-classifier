import json
import matplotlib.pyplot as plt
import numpy as np

def task5():

    # Open the json file containing details about the reviews and load the data
    f = open('/course/data/a1/reviews/HealthStory.json')
    data = json.load(f)

    # Collect the news_ids of the articles corresponding to each rating category
    rating_reviews = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for individual_review in data:
        if individual_review['rating'] in rating_reviews.keys():
            # Populate the data as a key-value pair within a dictionary
            rating_reviews[individual_review['rating']].append(individual_review['news_id'])

    # Opens the file containing the tweet IDs of tweets related to each article
    fp = open('/course/data/a1/engagements/HealthStory.json')
    # Loads the data collected
    tweet_info = json.load(fp)

    rating_tweets = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

    for rating in range(6):
        article_ids = set(rating_reviews[rating])
        num_articles = len(article_ids)
        
        # Find the tweet IDs of each article corresponding to a given rating using its article id
        for id in article_ids:
            if id in tweet_info.keys():
                # Add the list of tweet ids as values to the corresponding rating as a key
                rating_tweets[rating].extend(tweet_info[id]['tweets'])
                rating_tweets[rating].extend(tweet_info[id]['retweets'])
                rating_tweets[rating].extend(tweet_info[id]['replies'])
        
        # Calculate the unique number of tweets corresponding to each rating category
        rating_tweets[rating] = len(set(rating_tweets[rating]))/num_articles

    no_of_tweets = []
    rating = []

    # Create seperate lists containing rating categories and their respective number of tweets
    for tuple in rating_tweets.items():
        no_of_tweets.append(tuple[1])
        rating.append(tuple[0])
    
    # Assign the values in these lists to the x-axis and y-axis of the plot
    x_axis = rating
    y_axis = no_of_tweets

    # Specify the appropriate parameters and plot the graph
    plt.figure(figsize=(5, 5))
    plt.bar(x_axis,y_axis,color='red')
    plt.grid()
    plt.xlabel('Rating given')
    plt.ylabel('Number of tweets')
    plt.yticks(np.arange(0,400,25))
    plt.title('Average number of tweets for each article-rating group')
    plt.savefig("task5.png")           
     
    return
