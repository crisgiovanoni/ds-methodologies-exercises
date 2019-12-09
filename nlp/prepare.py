# Data Cleaning
import unicodedata
import re

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Basic and Additional Imports
import pandas as pd
import acquire

####### FUNCTIONS ########

def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    # remove anything not a space character, an apostrophy, letter, or number
    string = re.sub(r"[^a-z0-9'\s]", '', string)

    # convert newlines and tabs to a single space
    string = re.sub(r'[\r|\n|\r\n]+', ' ', string)
    string = string.strip()
    return string

def tokenize(string):
    tokenizer = ToktokTokenizer()
    return tokenizer.tokenize(string, return_str=True)

def stem(string):
    ps = PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    string_of_stems = ' '.join(stems)
    return string_of_stems

def lemmatize(string):
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string_of_lemmas = ' '.join(lemmas)
    return string_of_lemmas

def remove_stopwords(string, extra_words=[], exclude_words=[]):
    # Tokenize the string
    string = tokenize(string)

    words = string.split()
    stopword_list = stopwords.words('english')

    # remove the excluded words from the stopword list
    stopword_list = set(stopword_list) - set(exclude_words)

    # add in the user specified extra words
    stopword_list = stopword_list.union(set(extra_words))

    filtered_words = [w for w in words if w not in stopword_list]
    final_string = " ".join(filtered_words)
    return final_string

def prep_articles(df):
    df["original"] = df.content.copy()
    df["stemmed"] = df.content.apply(basic_clean).apply(stem)
    df["lemmatized"] = df.content.apply(basic_clean).apply(lemmatize)
    df["clean"] = df.content.apply(basic_clean).apply(remove_stopwords)
    return df

def prep_blog_posts():
    df = acquire.get_blog_posts()
    return prep_articles(df)

def prep_news_articles():
    df = acquire.get_news_articles()
    return prep_articles(df)

def prep_corpus():
    blog_df = prep_blog_posts()
    blog_df["source"] = "Codeup Blog"

    news_df = prep_news_articles()
    news_df["source"] = "InShorts News"

    return blog_df, news_df