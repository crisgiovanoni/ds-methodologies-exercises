import re
import unicodedata
import pandas as pd
import nltk

ADDITIONAL_STOPWORDS = ['r', 'u', '2', 'ltgt']

def clean(text):
    'A simple function to cleanup text data'
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') + ADDITIONAL_STOPWORDS
    text = (unicodedata.normalize('NFKD', text)
             .encode('ascii', 'ignore')
             .decode('utf-8', 'ignore')
             .lower())
    words = re.sub(r'[^\w\s]', '', text).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]

df = pd.read_csv('spam_clean.csv')
df.head()

# Create and explore bigrams for the spam data. Visualize them with a word cloud. How do they compare with the ham bigrams?
# Is there any overlap in the bigrams for the spam data and the ham data?
# Create and explore with trigrams (i.e. a n-gram with an n of 3) for both the spam and ham data.


df.text
bigrams = list(nltk.bigrams(df.text.str.split()))
bigrams