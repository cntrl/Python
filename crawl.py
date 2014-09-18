import requests
from bs4 import BeautifulSoup


def mainCrawler(query, max_pages):
    page = 1
    while page <= max_pages:
        url = ("http://jobsuche.monster.de/Jobs/"
               "?q=" + query + "&pg=" + str(page) + "&cy=de")
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
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


def getHyperlinks(item_url):
    Quellcode = requests.get(item_url)
    Quelltext = Quellcode.text
    soup = BeautifulSoup(Quelltext)
    for header in soup.findAll('title'):
        global jobtitel, href
        jobtitel = header.string
        href = ""

    for link in soup.findAll('a', {'data-track': 'ATB-AllJobs'}):
        href = link.get('href')
        href = href[47:len(href)]
        href = href.replace('+', ' ')
        print href

    heading = soup.findAll('h1')
    print(heading)

mainCrawler("Energiemanager", 1)
