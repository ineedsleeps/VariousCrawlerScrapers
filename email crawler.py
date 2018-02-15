import requests
import re

#get URL
url = input("Enter a URL (include 'http://'): ")

#connect to the URL
website = requests.get(url)

#read HTML
html = website.text

#get all the links
links = re.findall('"((https|ftp)s?://.*?)"', html)
emails = re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html)

#print number of links
print("\nFound {} links".format(len(links)))
for email in emails:
    print(email)
    
