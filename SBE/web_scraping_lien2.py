#importer les packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_all_pages():
    urls = []
    page_number = 1

    for i in range (26):
        i = f"https://www.goafricaonline.com/sn/annuaire/agences-de-communication?p={page_number}"
        page_number += 1
        urls.append(i)
    return urls


def parse_company(url) :
    #import code
    response=requests.get(url)
    response.encoding=response.apparent_encoding

    if response.status_code == 200:
        html = response.text

        f=open("scraping_link_2.html","w", encoding="utf-8")
        f.write(html)
        f.close()

        soup=BeautifulSoup(response.text,"html5lib")

    else:
        print("ERREUR:", response.status_code)

    # Getting all the article's tags
    articles_tag = soup.findAll("article")

    # Getting company's names with à for loop
    list_companys_names = []
    for a in articles_tag:
        name = a.find("a",class_="stretched-link font-bold text-16 t:text-20 text-black hover:text-black no-underline hover:no-underline").text
        activity_area = a.find("div",class_="text-14 text-brand-blue mb-4").text.strip()
        address = a.find("address",class_="text-14 text-gray-700 flex-1").text.strip()

        secteur = a.find("a",class_="z-10 text-13 t:text-14 text-gray-700 underline hover:no-underline")
        #getting the information in the tag <a>
        tel = secteur.get("href")
        #Phone number without the "tel:"
        new_tel = tel.replace("tel:", "")

        description = a.find("div",class_="block t:hidden text-gray-700 text-13")
        # if description != None :


        link = r"C:\xampp\htdocs\SBE\annuaire_entreprises.txt"
        with open(link, "a") as f:
            f.write(f"{name}\n")
            f.write(f"{activity_area}\n")
            f.write(f"{new_tel}\n")
            f.write(f"{description}\n\n")


def parse_all_company() :
    pages = get_all_pages()
    for page in pages:
        parse_company(url=page)
        print(f"On scrappe {page}")


parse_all_company()