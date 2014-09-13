import requests
import csv
from bs4 import BeautifulSoup


def monster_crawler(maxPages, stichwort, stadt, radius):
    page = 1
    outputList = []
    while page <= maxPages:
        if len(stadt) < 1:
            print("1")
            url = "http://berufsstart.monster.de/searchresults/home.aspx?pg=" + str(page) + "&q=" + stichwort
        elif len(stichwort) < 1:
            print("2")
            url = "http://berufsstart.monster.de/searchresults/home.aspx?pg=" + str(page) + "&where=" + stadt + "&rad=" + str(radius)
        elif len(stadt) < 1 and len(stichwort) < 1:
            print("3")
            url = "http://berufsstart.monster.de/searchresults/home.aspx?pg=" + str(page)
        else:
            print("4")
            url = "http://berufsstart.monster.de/searchresults/home.aspx?pg=" + str(page) + "&q=" + stichwort + "&where=" + stadt + "&rad=" + str(radius)

        sourceCode = requests.get(url)
        sourceText = sourceCode.text
        soup = BeautifulSoup(sourceText)
        for link in soup.findAll('a', {'target': '_blank'}):
            Stelle = link.string
            Link = link.get('href')
            hyperlink_crawler(Link)
            daten = [jobtitel, href]
            # print(daten)
            # print(Stelle)
            # print(href)
            outputList.append(daten)

        page += 1

    print(outputList)
    #out = csv.writer(open("jobs.csv","w"), delimiter=',')
    #out.writerow(outputList)




def hyperlink_crawler(item_url):
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
        # print href


anzahl = raw_input("Wieviele Seiten sollen gecrawled werden?")
query = raw_input("Nach welchem Stichwort soll gesucht werden?")
wo = raw_input("In welchem Ort soll gesucht werden?")
rad = raw_input("In welchem Radius?")

monster_crawler(int(anzahl), str(query), str(wo), int(rad))
