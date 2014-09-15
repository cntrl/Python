import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = ("http://jobsuche.monster.de/Jobs/"
               "?q=Energiemanager&pg=" + str(page) + "&cy=de")
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'slJobTitle fnt11'}):
            Stelle = link.string
            Link = link.get('href')
        # for image in soup.findAll('img', {'class': 'trovixCompanyLogo'}):
        #     Firma = image.get('alt', '')

            print("------")
            # print(Stelle)
            # print(Firma)
            print(Link)

        page += 1

trade_spider(1)
