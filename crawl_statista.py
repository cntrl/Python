import requests
from bs4 import BeautifulSoup


def mainCrawler(maxPages):
    page = 1
    while page <= maxPages:
        url = ("https://de.statista.com/statistik/suche/"
               "?accuracy=and&companies=1&itemsPerPage=25"
               "&q=Bau&subCategory=0&p=" + str(page))
        QuellCode = requests.get(url)
        QuellText = QuellCode.text
        soup = BeautifulSoup(QuellText)
        for link in soup.findAll('a', {'tabindex': '2'}):
            urlHyperlink = "https://de.statista.com/" + link['href']
            print urlHyperlink
            getHyperlinks(urlHyperlink)
            print(link.span)

        page += 1


def getHyperlinks(itemUrl):
    Quellcode = requests.get(itemUrl)
    Quelltext = Quellcode.text
    soup = BeautifulSoup(Quelltext)
    for header in soup.findAll('td'):
        print header

# Webcrawler starten.
mainCrawler(1)
