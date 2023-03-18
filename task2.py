import json 
import csv

def task2():

    # Define the rows and column titles of thr required csv file to be outputted 
    fields = ['news_id', 'news_title', 'review_title', 'rating', 'num_satisfactory']
    rows = []

    # Open the json file containing details about the reviews and load the data
    f = open('/course/data/a1/reviews/HealthStory.json')
    data = json.load(f)
    
    # Loop through each individual review in the json file
    for individual_review in data:

        # Allocate the required data within each review to seperate variables 
        news_id = individual_review['news_id']
        news_title = individual_review['original_title']
        review_title = individual_review['title']
        rating = individual_review['rating']

        # Count the total number of satisfactory criteria for each review
        num_satisfactory = 0
         
        # Loop through each category and see if it has been marked as "Satisfactory"
        for category in individual_review['criteria']:
            if category['answer'] == "Satisfactory":
                num_satisfactory += 1   

        # Add each row in the form of a list and aggregate all rows into a single nested list
        rows.append([news_id, news_title, review_title, rating, num_satisfactory])

    # Sort the rows in ascending order of news_id
    rows.sort(key=lambda x: x[0])

    # Create task2.csv and write the rows and columns to it
    with open('task2.csv', 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    return
