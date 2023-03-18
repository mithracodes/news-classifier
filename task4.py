import csv
import json
import matplotlib.pyplot as plt
import numpy as np

def task4():

    # Define the rows and column titles of the required csv file to be outputted 
    fields = ['news_source','num_articles','avg_rating']
    rows = []

    # Open the json file containing details about the reviews and load the data
    f = open('/course/data/a1/reviews/HealthStory.json')
    data = json.load(f)

    news_sources = []
    source_articles = []

    # Loop through each individual review in the json file
    for individual_review in data:
        # If a news source exists for that review, add it to the list
        if individual_review['news_source'] != None:
                # Ensure there is no duplication of news sources
                if individual_review['news_source'] not in news_sources:
                    news_sources.append(individual_review['news_source'])

    # Initialise other parameters to 0
    for source in news_sources:
        source_articles.append([source,0,0])
    
    # Calculate the total articles by each news source and sum up the ratings
    for individual_review in data:
       if individual_review['news_source'] in news_sources:
           for source_info in source_articles:
               if source_info[0] == individual_review['news_source']:
                   source_info[1] += 1
                   source_info[2] += individual_review['rating']

    # Find the average rating of each news source
    for source_info in source_articles:
        source_info[2] = source_info[2]/source_info[1]

    # Copy collected data into rows of csv
    rows = source_articles.copy()

    # Sort by ascending order of news source
    rows.sort(key=lambda x: x[0])
    rows.pop(0)

    # Create task4a.csv and write the rows and columns to it
    with open('task4a.csv', 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    
    average_article_ratings = {}

    # Open the csv file just created and read its rows
    with open('task4a.csv','r') as file:
        reader = csv.reader(file)

        for row in reader:

            # Check for news sources that have published atleast 5 articles
            if row[1].isnumeric() == True and int(row[1]) >= 5:
                average_article_ratings[row[0]]=row[2]
        
        # Sort by ascending order of news source
        average_article_ratings = sorted(average_article_ratings.items(), key = lambda x: x[1])
        source_names = []
        average_ratings = []

        # Create seperate lists containing news sources and their respective average ratings
        for tuple in average_article_ratings:
            source_names.append(tuple[0])
            average_ratings.append(tuple[1])
        
        # Assign the values in these lists to the x-axis and y-axis of the plot
        x_axis = source_names      
        y_axis = [round(float(rating),2) for rating in average_ratings]

        # Specify the appropriate parameters and plot the graph
        plt.figure(figsize=(20, 10))
        plt.barh(x_axis,y_axis)
        plt.grid()
        plt.xlabel('News Sources')
        plt.ylabel('Average Ratings')
        plt.xticks(np.arange(0,5,0.25))
        plt.title('Average rating of articles published by each news source')
        
        # Save the graph as 'task4b.png'
        plt.savefig("task4b.png")

    return
