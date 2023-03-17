# twitter-sentiment-analysis
An example of sentiment analysis on the twitter-samples dataset using the Logistic Regression Classification Algorithm.

The two python libraries:

- [matplotlib](http://www.matplotlib.org/) is a python library for plotting graphics
- [Stanford Natural Language Toolkit](http://www.nltk.org/) provides the natural language functionalities to build up a classifier.

# Dataset
The sample dataset from NLTK is separated into positive and negative tweets. It contains 5000 positive tweets and 5000 negative tweets exactly. The intention is to have a balanced dataset.

# Pre Processing

The preprocessing scripts modify the tweet's content to make possible further analysis. 

- Any URL is removed and substituted with a space " "
- Any @Username is removed
- Any not alphanumeric symbol is removed 
- Hashtags are substituted with the corresponding word
- The emoticon expressing sentiments is kept
- words are stemmed using the nltk PorterStemmer

# Feature Extractor
The preprocessing steps can be automated using the process tweets and build freqs module
Before building a classifier we need to extract all the features (words) contained in the tweet text.

Moreover, it is necessary to remove stop words. 
I also stripped out punctuation, digits, and any symbols that might be in the tweet text.

The stopwords can be downloaded with the nltk library using nltk. download('stopwords').
