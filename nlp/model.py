import unicodedata
import re

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import pandas as pd
import numpy as np

import acquire_news
import prepare

nltk.download()

#Acquire and Prep
news = acquire_news.make_new_request()
news = prepare.prep_articles(news,"content")

#Helper Functions
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


news["original"] = news.content.copy()

news["stemmed"] = news.content.apply(prepare.basic_clean)
news["stemmed"] = news.stemmed.apply(stem)

news["lemmatized"] = news.content.apply(prepare.basic_clean)
news["lemmatized"] = news.lemmatized.apply(lemmatize)



news.head()


