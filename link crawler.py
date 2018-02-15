import requests
import re
from urllib.parse import urljoin

#regex
link_re = re.compile(r'href="(.*?)"')

def crawl(url):
    req = requests.get(url)
    #check if successful
    if(req.status_code != 200):
        return[]

    #find links
    links = link_re.findall(req.text)

    print("\nFound {} links".format(len(links)))

    #search links for emails
    for link in links:
        #get an absolute URL for a link
        link = (url, link)
        print(link)

if __name__ == '__main__':
    crawl('http://www.askthesocialworker.org')
