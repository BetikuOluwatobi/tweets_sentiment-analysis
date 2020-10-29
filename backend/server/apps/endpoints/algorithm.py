import numpy as np
from .apps import EndpointsConfig
from nltk.corpus import stopwords
import re,string


class Logistic_Regression:
    def __init__(self):
        self.freq = EndpointsConfig.word_freq
        self.stemmer = EndpointsConfig.stemmer
        self.tokenizer = EndpointsConfig.tokenizer
        self.model = EndpointsConfig.model

    def process_tweet(self,tweet):
        '''
        Process tweet function.
        Input:
            tweet: a string containing a tweet
        Output:
            tweets_clean: a list of words containing the processed tweet
        '''
        stopwords_english = stopwords.words('english')
        # remove stock market tickers like $GE
        tweet = re.sub(r'\$\w*', '', tweet)
        # remove old style retweet text "RT"
        tweet = re.sub(r'^RT[\s]+', '', tweet)
        # remove hyperlinks
        tweet = re.sub(r'http\S+', '', tweet)
        # remove hashtags
        # only removing the hash # sign from the word
        tweet = re.sub(r'#', '', tweet)
        # tokenize tweets
        tweet_tokens = self.tokenizer.tokenize(tweet)

        tweets_clean = []
        for word in tweet_tokens:
            if (word not in stopwords_english and  # remove stopwords
                    word not in string.punctuation):  # remove punctuation
                # tweets_clean.append(word)
                stem_word = self.stemmer.stem(word)  # stemming word
                tweets_clean.append(stem_word)

        return tweets_clean

    #function helps in extracting useful features from text in 3 dimensional form
    def extract_features(self,p_tweet):
        sum_pos = 0
        sum_neg = 0
        for word in p_tweet:
            pos = self.freq.get((word,1),0)
            neg = self.freq.get((word,0),0)
            sum_pos += pos
            sum_neg += neg
        features = np.array([1,sum_pos,sum_neg])
        return features

    def predict_tweet(self,tweet):
        '''
        Input:
            tweet: tweet to predict
            theta:hyperparameter vector or matrix of form (3,1)
            freqs:dictionary of all words
        Output:
            y_pred: tweet's prediction
        '''
        clean_tweet = self.process_tweet(tweet)
        x = self.extract_features(clean_tweet)
        x = x.reshape(-1,3)

        #generate predictions
        y_pred = 'positive' if self.model.predict(x) == 1 else 'negative'
        return y_pred