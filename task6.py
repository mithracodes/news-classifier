import os,json
import re
import nltk
from nltk.corpus import stopwords

# Function that converts uppercase text to lowercase
def convert_to_lower(text):
    return text.group(0).lower()

def task6():

    distinct_words_id = {}

    # Define the path in which all the Article json files are located
    path_name = '/course/data/a1/content/HealthStory/'

    # Make a list of all the article files within the path
    for article in [filename for filename in os.listdir(path_name) if filename.endswith('.json')]:
        # Open each JSON file and load the data
        with open(path_name + article) as json_file:
            data = json.load(json_file)
            text = data["text"]
            
            # Replace all alphabetic characters with single-space characters using re library
            non_alpha_replace = re.sub(r'[^a-zA-Z\s]',' ', str(text))

            # Replace all spacing characters to single-space characters using re library
            space_replace = re.sub(r'\s+',' ',str(non_alpha_replace))
            
            # Convert all uppercase characters to lower case using re library and an external function
            lowercase_replace = re.sub(r'[A-Z]',convert_to_lower,space_replace)

            # Tokenise string into a list of words using space delimiter and remove multiple spaces
            tokenise_string = lowercase_replace.strip(" ").split(" ")
           
            # Remove all nltk English stop words from the list
            stop_words = set(stopwords.words('english'))
            remove_stop_words = [word for word in tokenise_string if word.lower() not in stop_words]

            # Ensure that single character long words are removed
            multiple_char = [word for word in remove_stop_words if len(word)>1]

            # Create a dictionary with each word in the remaining list as keys
            for word in multiple_char:
                # If word is already in dictionary, append the current news_id to its value
                if word in distinct_words_id.keys():  
                        distinct_words_id[word].append(str(article).replace('.json',''))              
                
                # Otherwise, add the word to the dictionary as a new key
                else:
                    # Add the current news_id as its first value
                    distinct_words_id[word] = [str(article).replace('.json','')]
                
                # Ensure that the list of articles for each word are in ascending order of news_id
                distinct_words_id[word] = sorted(list(set(distinct_words_id[word])))  

    # Ensure that words in dictionary are in ascending order by sorting            
    distinct_words_id = dict(sorted(distinct_words_id.items(), key = lambda x: (x[0],x[1])))
    
    # Appropriately format it and convert it into a json object
    json_object = json.dumps(distinct_words_id) 
   
    # Write the json object to a new json file called 'task6.json' as output
    with open("task6.json", "w") as outfile:
        outfile.write(json_object) 

    return

