import requests
from bs4 import BeautifulSoup


def mainCrawler(query, maxPages):
    page = 1
    while page <= maxPages:
        url = ("http://jobsuche.monster.de/Jobs/"
               "?q=" + query + "&pg=" + str(page) + "&cy=de")
        QuellCode = requests.get(url)
        QuellText = QuellCode.text
        soup = BeautifulSoup(QuellText)
        links = soup.findAll('a', {'class': lambda L: L and L.startswith
                                   ('slJobTitle')})
        for link in links:
            Link = link.get('href')
            print("------")
            print(Link)
            getHyperlinks(Link)
        for image in soup.findAll('img', {'class': 'trovixCompanyLogo'}):
            Firma = image.get('alt', '')
            print(image)
            print(Firma)

        page += 1


def getHyperlinks(itemUrl):
    Quellcode = requests.get(itemUrl)
    Quelltext = Quellcode.text
    soup = BeautifulSoup(Quelltext)
    for header in soup.findAll('title'):
        print header

    for link in soup.findAll('a', {'data-track': 'ATB-AllJobs'}):
        companyName = link.get('href')
        companyName = companyName[47:len(companyName)]
        companyName = companyName.replace('+', ' ')
        companyName = companyName.replace('%26', '&')
        companyName = companyName.replace('%c3%bc', 'ue')
        print companyName

    heading = soup.findAll('h1')
    print(heading)


# Webcrawler starten.
# Argument 1 gibt den gewünschten Suchbegriff an,
# Argument 2 die Anzahl an zu crawlenden Suchseiten.
page = raw_input("Wieviele Seiten sollen gecrawled werden? ")
query = raw_input("Nach welchem Suchbegriff soll gesucht werden? ")
mainCrawler(query, page)
