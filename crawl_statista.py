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
        # print soup
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

    # for link in soup.findAll('a', {'data-track': 'ATB-AllJobs'}):
    #     companyName = link.get('href')
    #     companyName = companyName[47:len(companyName)]
    #     companyName = companyName.replace('+', ' ')
    #     companyName = companyName.replace('%26', '&')
    #     companyName = companyName.replace('%c3%bc', 'ue')
    #     print companyName
    #
    # heading = soup.findAll('h1')
    # print(heading)
    #

# Webcrawler starten.
# Argument 1 gibt den gewünschten Suchbegriff an,
# Argument 2 die Anzahl an zu crawlenden Suchseiten.
mainCrawler(1)
