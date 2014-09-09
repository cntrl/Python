import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://berufsstart.monster.de/searchresults/home.aspx?q=Energiemanagement&pg=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'target': '_blank'}):
            Stelle = link.string
            Link = link.get('href')
        for item_name in soup.findAll('div', {'class': 'fnt16'}):
            Firma = item_name.string

            print("------")
            print(Stelle)
            print(Firma)
            print(Link)


        page += 1

trade_spider(2)
