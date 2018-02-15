import requests
import re
from bs4 import BeautifulSoup as bs4
import time

def cl(word):
    url_base = ('https://collegestation.craigslist.org/search/sss')
    params = dict(query=keyword, sort='relevant')
    rsp = requests.get(url_base, params=params)
    html = bs4(rsp.text, 'html.parser')
    list1 = []
    list1 = html.find_all('p', attrs={'class': 'result-info'})
    for l in list1:
        price = l.find('span', attrs={'class': 'result-price'})
        if price == None:
            price = 'unknown'
        else:
            price = str(price.text)
        date = l.find('time', attrs={'class': 'result-date'})
        date = date.text
        link = l.find('a', attrs={'class': 'result-title'})
        text = link.text
        link = link.get('href')
        desc = text+"\n "+price+", "+date+"\n"+link
        print(desc)


if __name__ == '__main__':
    keyword = input("What would you like to search Craigslist for? ")
    cl(keyword)
