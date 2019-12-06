# Define a function named basic_clean. It should take in a string and apply some basic text cleaning to it:

# Lowercase everything
# Normalize unicode characters
# Replace anything that is not a letter, number, w

# Data Cleaning
import unicodedata
import re

# Normalizing
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

# Basic and Additional Imports
import pandas as pd
import acquire

####### FUNCTIONS ########

# Lower Case
def convert_to_lowercase(series):
    return series.str.lower()

# ASCII
def normalize(string):
    return unicodedata.normalize("NFKD", string).encode("ascii","ignore").decode("utf-8","ignore")

def normalize_column(series):
    return series.apply(normalize)

# Special Characters
def remove_special(string):
    return re.sub(r"[^a-z0-9'-\s]","", string)

def remove_special_on_columns(series):
    return series.apply(remove_special)

# FINAL ormalcy functions
def format_text(series):
    return series.pipe(convert_to_lowercase).pipe(normalize_column).pipe(remove_special_on_columns)

####### TEST ##########
df = acquire.get_news_articles()
cont = df.content.copy()
cont = format_text(cont)

## TEST FUNCTIONS HERE ##
