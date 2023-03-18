# news-classifier

## Overview

This project aims to identify credible health-related news sources from a dataset of 1,000+ news articles, reviews, and tweets. Using natural language processing techniques like sentiment analysis, topic modeling, and named entity recognition, it analyzes linguistic patterns to distinguish good and bad news sources. By comparing different news outlets based on their reporting accuracy, it further provides insights into credible and trustworthy health-related news sources. This is particularly important as false or misleading health-related news can have severe consequences. The results can benefit journalists, policy makers, and researchers who rely on accurate information.

## Dataset

The dataset consists of more than 1,000 health-related news articles, the reviews of these articles, and tweets about the new articles.

### News articles

Each of the news articles is stored in a file in the `/content/HealthStory` folder. The name of each file corresponds to the ID of the article and is in the format `story_reviews_xxxxx.json`, where each x is a digit; for example, `story_reviews_00001.json` contains the news article of ID `story_reviews_00001`.

### News reviews

Each article was independently reviewed by at least one expert, based on a list of criteria. Against each criterion, the article receives a rating of *satisfactory*, *not satisfactory* or *not applicable*, and an explanation for the rating. Each article is also assigned an overall rating between 0 (least accurate) to 5 (most accurate).

All reviews are stored in a single file: `/reviews/HealthStory.json`.

### Tweets

The IDs of tweets about the news articles are recorded in `/engagements/HealthStory.json`. The file contains a dictionary with keys being article IDs, and the corresponding values containing tweets represented by a unique integer. 

## Tasks

To run each task, open the terminal and execute the command `python main.py tasknumber`.

### Loading Data (Task 1)

The program includes a function called task1() which can be found in task1.py. When executed, the function outputs a JSON file called task1.json in the following format:

```powershell
{
  "Total number of articles": X,
  "Total number of reviews": Y,
  "Total number of tweets": Z
}
```

Here, `X` represents the total number of news articles, `Y` represents the total number of reviews, and `Z` represents the total number of tweets.

### Data aggregation (Task 2)

The reviews contain an ID field called `news_id` corresponding to the ID of the news article that helps in matching the review with the news article.

The function task2() which can be found in task2.py, when executed combines the articles with their reviews to work out how many “satisfactory” ratings that article receives, out of a total of 10 criteria. The output of this function is saved to a CSV file called task2.csv which contains the following headings: `news_id, news_title, review_title, rating, num_satisfactory`.

Each row in the file contains the details of one article, where:

- `news_id` is the ID of the news article in the format `story_reviews_xxxxx`
* `news_title` is the title of the news article
+ `review_title` is the title of the review article
- `rating` is the overall rating of the article (between 0 and 5)
* `num_satisfactory` is the total number of criteria (between 0 and 10) that are satisfactory

The rows in `task2.csv` are sorted in ascending order of `news_id`. 

### Meta-data extraction (Task 3)

Each news article comes with a `publish_date` field which specifies when the article was published. The field is in the millisecond precision format, which is a floating point number. The program includes a function called `task3()` which can be found in `task3.py`.

`task3()` performs the following two sub-tasks:

1. Extract the year, month, and day components from the `publish_date` of each article, and output a CSV file called `task3a.csv`, which contains the following headings: `news_id, year, month, day`. Each row contains the ID of an article in the format story_reviews_xxxxx, and the year, month, day on which it was published. 

2. Count the number of articles in each calendar year in the dataset, and output a file called `task3b.png`, describing the yearly article counts using an appropriately chosen graph. The articles for which the publish date is unspecified are excluded from the output.

### Assessing the credibility of news agencies (Task 4)

The program compares the average rating of articles published by each news source. Each review contains a `news_source` field, which indicates where the article was published. 

The `task4()` function is implemented in `task4.py` to perform the following subtasks:

- Output a csv file called `task4a.csv`, which contains the following headings: `news_source, num_articles, avg_rating`. Each row contains details about one news source. The rows in `task4a.csv` are sorted in ascending order of `news_source`.

* Output a plot called `task4b.png` comparing the average ratings of all news sources that have at least 5 articles. The axes of the plot are sorted in a way that the most and least credible news sources are easily identified.

### Assessment of credibility against popularity (Task 5)

The function `task5()` in `task5.py` which outputs a file called `task5.png` comparing the average number of tweets for each article-rating group. 

### Text processing (Task 6)

News articles often contain non-alphabetic characters, emojis, and other elements that make them difficult to process. This task aims to preprocess the content of the news articles to make analysis easier.

The program implements the function `task6()` in `task6.py` that performs the following preprocessing steps on the text field of the articles:

- Converts all non-alphabetic characters (e.g. numbers, punctuation) to single-space characters, except for spacing characters (e.g. whitespaces, tabs, newlines).

* Converts all spacing characters into single-space characters and ensures that only one whitespace character exists between each token.

+ Changes all uppercase characters to lowercase.

- Tokenizes the resulting string into a list of words using the space delimiter.

* Removes all stop words in nltk's list of English stop words from the resulting list.

+ Removes all remaining words that are only a single character long from the resulting list.

- Once steps 1-6 are complete, builds a vocabulary of distinct words as a JSON object and outputs it to a file called `task6.json`. Each key is a word, and the value is an array of the news_id of articles containing that word. The entries in `task6.json` are in ascending order of the word, and the list of articles for each word is also in ascending order of `news_id`. The format of each key-value pair of the JSON object is `"word": ["story_reviews_xxxxx", "story_reviews_yyyyy"]`.

* The program implements vocabulary creation efficiently, with a runtime of no more than 45 seconds. Excessively long execution time results in a deduction of 1 mark. The use of the re package is recommended for efficiency.

### Detection of indicative words in fake news (Task 7)

This task aims to detect the most indicative words of fake news by analyzing the dataset provided. An article is considered real if its rating is at least 3, while a fake news article has a rating below 3.

To calculate the odds ratio, we first define the probability that a word w appears in a real news article as 

![image](https://user-images.githubusercontent.com/95140934/226115087-1e13fcdf-dfda-4603-a32a-21216a747fa4.png)

Further, the odds that a word w appears in a real article is defined as
![image](https://user-images.githubusercontent.com/95140934/226115137-5b4fd289-7c83-4ba8-aebe-00bb0778d8dd.png)

Similarly, *pf(w)* and *of(w)* is defined for each w in fake news articles.

To avoid odds of 0 or infinity, words w such that *pr(w) ∈ {0.0, 1.0}* or *pf(w) ∈ {0.0, 1.0}* are excluded. The `log_odds_ratio` (for fake news) is defined as 
![image](https://user-images.githubusercontent.com/95140934/226115219-b077d75a-cba5-4029-b353-10fa683ed7c2.png)

where *or(w)* is the odds ratio for fake news, given by
![image](https://user-images.githubusercontent.com/95140934/226115243-e35e5bb2-e044-4280-80dd-51911a4a5082.png)

The log_odds_ratio (for fake news) is positive if *or(w)* > 1 and is negative if *or(w)* < 1. The `log_odds_ratio` is 0 if *or(w)* = 1, which indicates that w is not more representative of fake nor of real news.

The `task7()` function in `task7.py` implements the following tasks:

1. Calculates the `log_odds_ratio`, for fake news, for each word in the vocabulary.
2. Excludes the words where *p<sub>r</sub>* or *p<sub>f</sub>* is exactly 0 or 1 (words that appear exclusively in real news or fake news).
3. Excludes the words which appear in fewer than 10 articles and words that appear in all articles.
4. Outputs a csv file called `task7a.csv` with the following headings: `word, log_odds_ratio`. Each row represents a word in the vocabulary and the log odds ratio for fake news of that word. The value of `log_odds_ratio` is rounded to 5 digits from the decimal point. The entries in `task7a.csv` are in ascending order of word.
5. Outputs a file called `task7b.png` which contains an appropriately chosen graph, showing the distribution of the log odds ratios for all words.
6. Outputs a file called `task7c.png` which contains an appropriately chosen graph, showing the top 15 words with the highest odds ratios for fake news, and the top 15 words with the lowest odds ratios.

***Note: This is my submission for *Assignment 1 of COMP20008 Elements of Data Processing in Sem 1 2022*. ***
