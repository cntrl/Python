import requests
from bs4 import BeautifulSoup


def hyperlink_crawler(item_url):
    sourceCode = requests.get(item_url)
    sourceText = sourceCode.text
    soup = BeautifulSoup(sourceText)
    spans = soup.findAll('span', {'itemprop': 'reviewCount'})
    for span in spans:
        print span.string
    # desc = soup.findAll("p")
    # print(desc)

i = 1
url = "http://www.yelp.de/search?find_desc=Koreanisches+Restaurant&find_loc=Berlin&ns=1"
sourceCode = requests.get(url)
sourceText = sourceCode.text
soup = BeautifulSoup(sourceText)
for link in soup.findAll('a', {'class': 'biz-name'}):
    namen = link.string
    link = "http://www.yelp.de" + link.get('href')
    hyperlink_crawler(link)
    print(i, namen)
    print(link)
    i += 1
