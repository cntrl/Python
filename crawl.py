import requests
from bs4 import BeautifulSoup


def get_subsites(item_url):
    sourceCode = requests.get(item_url)
    sourceText = sourceCode.text
    soup = BeautifulSoup(sourceText)
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


def main_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = ("http://jobsuche.monster.de/Jobs/"
               "?q=Energiemanager&pg=" + str(page) + "&cy=de")
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        links = soup.findAll('a', {'class': lambda L: L and L.startswith
                                   ('slJobTitle')})
        for link in links:
            Link = link.get('href')
            print("------")
            print(Link)
            get_subsites(Link)
        for image in soup.findAll('img', {'class': 'trovixCompanyLogo'}):
            Firma = image.get('alt', '')
            print(image)
            print(Firma)

        page += 1


main_crawler(1)
