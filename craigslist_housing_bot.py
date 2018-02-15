import requests
import re
from bs4 import BeautifulSoup as bs4

def cl(bed, bath, mini_price, maxi_price):
    url_base = ('https://collegestation.craigslist.org/search/hhh')
    params = dict(query="apartment", sort='relevant', min_price=mini_price, max_price=maxi_price, min_bedrooms=bed, min_bathrooms=bath)
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
    print("I see you are looking for an apartment.")
    beds = input("How many bedrooms would you like? ")
    baths = input("How many bathrooms would you like? ")
    min_price = input("What is the minimum price you'd like to pay? ")
    max_price = input("What is the maximum price you'd like to pay? ")
    cl(beds, baths, min_price, max_price)
