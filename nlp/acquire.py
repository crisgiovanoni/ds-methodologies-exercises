from requests import get
from bs4 import BeautifulSoup
import os

def make_dictionary_from_article(url):
    #Connect to internet
    url_path = url
    headers = {'User-Agent': 'Bayes-DS'}
    response = get(url_path, headers=headers)

    #Soup the title and body of article
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #get title through selector or html title element 
    title = soup.title

    body = soup.find('div',class_="mk-single-content")
    body = body.text

    return {
        "title": title,
        "body": body
    }

def get_blog_articles():
    urls = [
        "https://codeup.com/codeups-data-science-career-accelerator-is-here/",
        "https://codeup.com/data-science-myths/",
        "https://codeup.com/data-science-vs-data-analytics-whats-the-difference/",
        "https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/",
        "https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/",
    ]

    full_articles = []
    for url in urls:
        full_articles.append(make_dictionary_from_article(url)) 

    return full_articles
