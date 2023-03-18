import csv,json,os
from task6 import task6
import math
import glob
import matplotlib.pyplot as plt
import numpy as np

def task7():

    # Import json file containing the vocabulary of distinct words from Task 6
    task6 = open('/home/task6.json')
    distinct_words = json.load(task6)

    # Extract all the distinct words into a list
    distinct_words_list = list(distinct_words.keys())

    # Define the rows and column titles of thr required csv file to be outputted 
    fields = ['word', 'log_odds_ratio']
    rows = []

    # Distinguish between fake and real articles, count them and store it in a dictionary
    real_or_fake = {}
    real_articles = 0
    fake_articles = 0
    
    # Calculate the total number of articles published
    total_articles = len(glob.glob1('/course/data/a1/content/HealthStory/',"*.json"))

    # Open the json file containing details about the reviews and load the data
    f = open('/course/data/a1/reviews/HealthStory.json')
    data = json.load(f)
    
    # Loop through each individual review in the json file
    for individual_review in data:

        rating = individual_review['rating']

        # Find real articles 
        if rating >= 3:
            # Store their news_id in a dictionary
            real_or_fake[individual_review['news_id']] = 'REAL'
            # Count the number of real articles
            real_articles += 1
        
        # Find fake articles
        else:
            # Store their news_id in a dictionary
            real_or_fake[individual_review['news_id']] = 'FAKE'
            # Count the number of fake articles
            fake_articles += 1
    
    odds_ratios_list = []

    # For each distinct word
    for word in distinct_words_list:

        # Find the number of real and fake articles 
        real_word_articles = 0
        fake_word_articles = 0

        # Find the news_id of all articles that word appears in
        article_list = distinct_words[word]

        # Filter only the words that appear in 10 or more articles and do not appear in all articles 
        if (len(article_list) >= 10) and (len(article_list)!=total_articles):
            for id in article_list:
                # Count the number of fake and real articles that the word appears in
                if real_or_fake[id] == 'REAL':
                    real_word_articles += 1
                else:
                    fake_word_articles += 1
            
            # Find the probability of the word appearing in a real article
            prob_real_article = real_word_articles/real_articles
            # Find the probability of the word appearing in a fake article
            prob_fake_article = fake_word_articles/fake_articles

            # Exclude the words where the probability is exactly 0 or 1
            if (prob_real_article not in {0.0,1.0}) and (prob_fake_article not in {0.0,1.0}):

                # Calculate the odds of that word appearing in a real article
                odds_real_article = (prob_real_article)/(1-prob_real_article)
                # Calculate the odds of that word appearing in a fake article
                odds_fake_article = (prob_fake_article)/(1-prob_fake_article)

                # Calculate the odds ratio for fake news
                odds_ratio = odds_fake_article/odds_real_article
                # Convert it into log odds ratio 
                log_odds_ratio = round(math.log10(odds_ratio),5)

                # Add the word and its log odds ratio as a row to the csv file
                rows.append([word,log_odds_ratio])

                # Create a nested list containing each word and its odds ratio
                odds_ratios_list.append([word,odds_ratio])
   
    # Sort the entries of the csv file in ascending order of word
    rows.sort(key=lambda x:x[0])

    # Create task7a.csv and write the rows and columns to it
    with open('task7a.csv', 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    log_odds_ratios = []

    # Open task7a.csv and read its content
    with open('task7a.csv','r') as file:
        reader = csv.reader(file)

        for row in reader:

            # Create a list containing the corresponding log odds ratios of all distinct words in alphabetic order
            log_odds_ratios.append(row[1])

    # Remove the header row and convert values into float for easier plotting
    log_odds_ratios.pop(0)
    log_odds_ratios = [float(x) for x in log_odds_ratios]

    # Plot a boxplot showing the distribution of the log odds ratios for all words
    task7b = plt.figure("task7b")
    plt.boxplot(log_odds_ratios,patch_artist=True,boxprops=dict(facecolor='#76EEC6'),medianprops=dict(color='red'),whiskerprops=dict(color='#00008B'),flierprops=dict(markeredgecolor='#EEB422'))
    
    # Specify the appropriate parameters and plot the figure
    plt.title("Distribution of the log odds ratio of all words")
    plt.ylabel('Log Odds Ratio')
    plt.yticks(np.arange(-1,1.25,0.25))
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    plt.grid()
    
    # Save the figure as 'task7b.png' and output it
    plt.savefig('task7b.png')

    # Sort the list containing odds ratios of all words in ascending order
    odds_ratios_list.sort(key=lambda x: x[1])

    # Find the top 15 words with the lowest odds ratios for fake news
    bottom_15_words = []
    bottom_15_ratios = []
    
    count = 0

    # Retrieve the first 15 elements and add it to a list
    for row in odds_ratios_list:
        if count < 15:
            bottom_15_words.append(row[0])
            bottom_15_ratios.append(row[1])
            count += 1

    # Sort the list containing odds ratios of all words in descending order
    odds_ratios_list.sort(key=lambda x: x[1],reverse=True)
    
    # Find the top 15 words with the lowest odds ratios for fake news
    top_15_words = []
    top_15_ratios = []

    count = 0

    # Retrieve the first 15 elements and add it to a list
    for row in odds_ratios_list:
        if count < 15:
            top_15_words.append(row[0])
            top_15_ratios.append(row[1])
            count += 1
    
    # Plot a scatter plot showing the top 15 words with the highest and lowest odds ratios respectively
    task7c = plt.figure("task7c",figsize=(35,7))

    # Specify the appropriate parameters and plot the figure
    plt.ylabel("Odds Ratios")
    plt.ylim([-1, 7.5]) 
    plt.scatter(top_15_words,top_15_ratios, c = "green",label = "Top 15 words with the highest odds ratios")
    plt.scatter(bottom_15_words,bottom_15_ratios, c = "red",label="Top 15 words with the lowest odds ratios")
    
    # Assign the respective word as the label for the data point
    for word in top_15_words:
        index = top_15_words.index(word)
        plt.annotate(word, xy=(word,top_15_ratios[index]), xytext = (0.5,-15),ha='center',textcoords="offset points")
    
    for word in bottom_15_words:
        index = bottom_15_words.index(word)
        plt.annotate(word, xy=(word,bottom_15_ratios[index]), xytext = (-0.5,15),ha='center',textcoords="offset points")

    # Set other parameters such as title and gridlines for the plot
    plt.yticks(np.arange(-0.5,7.5,0.25))
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    plt.title('Comparison of Top 15 words with the highest and lowest odds ratios')
    plt.legend()
    plt.grid()

    # Save the plot as 'task7c.png' and output it
    plt.savefig('task7c.png')
    return
