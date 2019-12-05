from requests import get
from bs4 import BeautifulSoup
import os

#Starters
url = "https://codeup.com/codeups-data-science-career-accelerator-is-here/"
url = "https://codeup.com/data-science-myths/"
url = "https://codeup.com/data-science-vs-data-analytics-whats-the-difference/"
headers = {'User-Agent': 'Bayes DS'}
response = get(url, headers=headers)

#Sanity check if we got the right website
print(response.text)

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.select('#mk-page-introduce > div > h1')
title = title[0].get_text()

title

article = soup.find('div',class_="mk-single-content")
article = article.text

title
article

def make_dictionary_from_article(url):
    #Connect to internet
    url_path = url
    headers = {'User-Agent': 'Bayes-DS'}
    response = get(url_path, headers=headers)

    #Soup the title and body of article
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.select('#mk-page-introduce > div > h1')
    title = title[0].get_text()

    body = soup.find('div',class_="mk-single-content")
    body = body.text

    return {
        "title": title,
        "body": body
    }
    
    

# https://codeup.com/codeups-data-science-career-accelerator-is-here/
# https://codeup.com/data-science-myths/
# https://codeup.com/data-science-vs-data-analytics-whats-the-difference/
# https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/
# https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/


def make_dictionary_from_article(url):
    # make the request to the url variable
    # make a "soup" variable
    # isolate the title of the article, store it as a string called "title"
    # isolate the body text of the article (buy CSS selector), name the variable "body"
    
    return {
        "title": title,
        "body": body
    }
​
​
def get_blog_articles():
    urls = [
        "https://codeup.com/codeups-data-science-career-accelerator-is-here/",
        "https://codeup.com/data-science-myths/",
        "https://codeup.com/data-science-vs-data-analytics-whats-the-difference/",
        "https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/",
        "https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/",
    ]
​
    output = []
    
    for url in urls:
        output.append(make_dictionary_from_article(url))
​
    return output