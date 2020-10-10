# twitter-sentiment-analysis
An example of sentiment analysis on Twitter using the labels "postive" and "negative".

To complete the analysis exploits two python libraries:

- [matplotlib](http://www.matplotlib.org/), which is python library for plotting graphics
- [Stanford Natural Language Toolkit](http://www.nltk.org/), which provides the natural languages functionalities to build up classifier.

# Dataset
The dataset can be gotten with nltk.download('twitter-samples')

# Pre Processing

The preprocessing scripts modifies the tweets content in order to make possible the further analysis. 

- Any url is removed and substituted with the with a space " "
- Any @Username is removed
- Any not alphanumeric symbol is removed 
- Hashtags are substituted with the corresponding word
- The emoticon expressing sentiments are kept
- words are stemmed using the nltk PorterStemmer

# Feature Extractor
The preprocessing steps can be automated using the process tweets and build freqs module
Before building a classifier we need to extract all the features (word) contained in the tweet text.

Moreover, is necessary to remove any stop words. 
I also stripped out punctuation, digits, and any symbols that might be still in the tweet text.

The stopwords can be downloaded with the nltk library using nltk.download('stopwords').
