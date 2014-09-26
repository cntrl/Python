import requests
import csv
from bs4 import BeautifulSoup

global num
global inventory
num = 0
inventory = {}


def mainCrawler(maxPages):
    page = 1
    global num
    global inventory
    while page <= maxPages:
        url = ("https://de.statista.com/statistik/suche/"
               "?accuracy=and&companies=1&itemsPerPage=3"
               "&subCategory=0&p=" + str(page))
        QuellCode = requests.get(url)
        QuellText = QuellCode.text
        soup = BeautifulSoup(QuellText)
        branche = soup.find('p', attrs={'class': 'statDesc'})
        brancheText = branche.text
        for link in soup.findAll('a', {'tabindex': '2'}):
            # span = link.find('span')
            # Firmenname = span.contents
            urlHyperlink = "https://de.statista.com/" + link['href']
            getHyperlinks(urlHyperlink, brancheText)
        page += 1
        num += 1
    print inventory
    with open('test.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(inventory.items())


def getHyperlinks(itemUrl, brancheText):
    global num, inventory
    Quellcode = requests.get(itemUrl)
    Quelltext = Quellcode.text
    soup = BeautifulSoup(Quelltext)
    zwires = []
    zahl = 0
    for header in soup.findAll('td'):
        zahl += 1
    if zahl == 18:
        for header in soup.findAll('td'):
            if zahl % 2 != 0:
                zwires.append(header.contents)
            zahl += 1
        zwires.append(brancheText)
        spans = soup.findAll('span', attrs={'itemprop': 'title'})
        for span in spans:
            zwires.append(span.contents)
    inventory[str(num)] = zwires
    print num
    print zwires

# Webcrawler starten.
mainCrawler(100)
