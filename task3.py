import os,json,csv
import datetime,time
import matplotlib.pyplot as plt
import numpy as np

def task3():

    # Define the rows and column titles of the required csv file to be outputted 
    fields = ['news_id','year','month','day']
    rows = []

    # Define the path in which all the Article json files are located
    path_name = '/course/data/a1/content/HealthStory/'

    # Make a list of all the article files within the path
    for article in [filename for filename in os.listdir(path_name) if filename.endswith('.json')]:
        # Open each JSON file and load the data
        with open(path_name + article) as json_file:
            data = json.load(json_file)
            
            # Only include those articles where publish date is specified
            if data["publish_date"] != None:

                # Extract news_id from the file name
                news_id = str(article).replace('.json','')

                # Convert publish_date into datetime format
                date_time = datetime.datetime.fromtimestamp(data["publish_date"])
                
                # Extract day, month and year from the datetime element
                year = date_time.strftime("%Y")
                month = date_time.strftime("%m")
                day = date_time.strftime("%d")

                # Add each row in the form of a list and aggregate all rows into a single nested list
                rows.append([news_id, year, month, day])
    
    # Sort the rows in ascending order of news_id
    rows.sort(key=lambda x: x[0])

    # Create task3a.csv and write the rows and columns to it
    with open('task3a.csv', 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    
    year_articles = {}

    # Open the csv file just created and read its rows
    with open('task3a.csv','r') as file:
        reader = csv.reader(file)

        # Create a dictionary with the years as keys
        for row in reader:
            # Initialise all values to 0
            if row[1] not in year_articles.keys():
                year_articles[row[1]] = 1

            # If an article was published in that year    
            else:
                # Increment the corresponding value for each year
               year_articles[row[1]] += 1 
        
        # Remove the 'year' heading key from the dictionary
        year_articles = {key:val for key, val in year_articles.items() if key != 'year'}        
        # Sort dictionary in increasing order of years
        year_articles = sorted(year_articles.items(), key = lambda x: x[0])
        
        years = []
        articles = []

        # Segregate dictionary into 'year' and corresponding 'number of articles' lists
        for tuple in year_articles:
            years.append(tuple[0])
            articles.append(tuple[1])

        # Assign the lists to the x-axis and y-axis of the plot
        x_axis = years
        y_axis = articles

        # Specify the appropriate parameters and plot the graph
        plt.bar(x_axis,y_axis,color=['brown'])
        plt.grid()
        plt.xlabel('Years')
        plt.ylabel('Number of articles')
        plt.yticks(np.arange(0,250,25))
        plt.title('Number of articles published each year (2009-2018)')
        
        # Save the graph as 'task3b.png'
        plt.savefig("task3b.png")
            
    return
