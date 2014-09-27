import requests
import csv
from bs4 import BeautifulSoup

global num
global inventory
num = 1
inventory = {}


def mainCrawler(startPage, maxPages):
    page = startPage
    global num
    global inventory
    while page <= maxPages:
        url = ("https://de.statista.com/statistik/suche/"
               "?accuracy=and&companies=1&itemsPerPage=3"
               "&subCategory=0&p=" + str(page))
        QuellCode = requests.get(url)
        QuellText = QuellCode.content
        soup = BeautifulSoup(QuellText)
        branche = soup.find('p', attrs={'class': 'statDesc'})
        brancheText = branche
        for link in soup.findAll('a', {'tabindex': '2'}):
            # span = link.find('span')
            # Firmenname = span.contents
            # print Firmenname
            urlHyperlink = "https://de.statista.com/" + link['href']
            getHyperlinks(urlHyperlink, brancheText.text)
        page += 1
        num += 1
    print inventory
    filename = "%s-%s.csv" % (str(startPage), str(maxPages))
    with open(filename, 'w') as f:
        w = csv.writer(f)
        w.writerows(inventory.items())

    # w = csv.writer(open(filename, 'wb'))
    # for key, value in inventory.items():
    #     w.writerows([key, value])

def getHyperlinks(itemUrl, brancheText):
    global num, inventory
    Quellcode = requests.get(itemUrl)
    Quelltext = Quellcode.content
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
# Argument 1 = Erste Seite, Argument 2 = Letzte Seite
mainCrawler(1, 2)
