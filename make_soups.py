'''
Description: This file requests access to webpage links and creates
                BeautifulSoup objects.
'''


###########################
### DEF NEW FUNCTION: 2 ###
### Store html in beautiful soup

import requests
from bs4 import BeautifulSoup

def make_soups(link):

    # Getting a URL:
    r = requests.get(link)
    
    # Print success code when links are accessed (Success code: 200)
    print(r)

    # Getting URL content in HTML:
    soup = BeautifulSoup(r.content, 'html.parser')


    # Finding all instances of the "o-chart-results-list__item" class:
    s = soup.find_all("li", class_="o-chart-results-list__item")
    print(len(s))


    # Finding all instances of the "o-chart-credits*" class, to get the
    # artist labels:
    c = soup.find_all("div", class_ =
        "o-chart-credits // lrv-u-margin-t-2 lrv-u-margin-t-125@mobile-max")

    
    print('Successful soup making!')

    return s, c
