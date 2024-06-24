#importer les packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

#saisir l'url
url="https://www.goafricaonline.com/sn/nouvelles-societes-du-senegal"

#import le de code de la page
response=requests.get(url)
response.encoding=response.apparent_encoding

if response.status_code == 200:
    html = response.text

    f=open("sbe.html","w")
    f.write(html)
    f.close()

    soup=BeautifulSoup(response.text,"html5lib")

else:
    print("ERREUR:", response.status_code)




###################  SCRAPING ON THE WHOLE PAGE  ###################

# Getting all the article's tags
articles_tag = soup.findAll("article")

# Getting company's names with à for loop
list_companys_names = []
for a in articles_tag:
    nom = a.find("a",class_="stretched-link font-bold text-16 t:text-20 text-black hover:text-black no-underline hover:no-underline").text
    list_companys_names.append(nom)

# # print(list_companys_names)

#récupérer les secteurs d'activité de toutes les entreprises avec une boucle for
activity_area_list = []
for a in articles_tag:
    secteur = a.find("div",class_="text-14 text-brand-blue mb-4").text.strip()
    activity_area_list.append(secteur)

# print(activity_area_list)


#getting the company's address
address_list = []
for a in articles_tag:
    address = a.find("address",class_="text-14 text-gray-700 flex-1").text.strip()
    address_list.append(address)

# print(address_list)

#getting the company's phone number
tel_list = []
for a in articles_tag:
    try :
        secteur = a.find("a",class_="z-10 text-13 t:text-14 text-gray-700 underline hover:no-underline")
        #Récupérer le contenu de l'attribut href de la balise <a> grâce à la fonction get()
        tel = secteur.get("href")
        #Phone number without the "tel:"
        new_tel = tel.replace("tel:", "")
    except AttributeError as e: 
                new_tel = "Vide"

    tel_list.append(new_tel)

# print(tel_list)

#getting the company's descriptions
company_description_list = []
for a in articles_tag:
    description = a.find("div",class_="block t:hidden text-gray-700 text-13")
    if description == None :
        company_description_list.append("Sans description")
    else:
        company_description_list.append(description.text)



###################  STORE INFORMATION TEST INTO DATABASE  ###################

# Calling DataFrame constructor on list
dictionnary = {'nom':list_companys_names, 'adresse':address_list, 'telephone':tel_list, 'description':company_description_list, 'secteur':activity_area_list}
df_test = pd.DataFrame.from_dict(dictionnary, orient='index')
df_test = df_test.transpose()
# df_test = pd.DataFrame(dictionnary)
print(df_test)


# # importing sql library
# from sqlalchemy import create_engine

# # engine = create_engine("url_object",echo=False)
# engine = create_engine("mysql+pymysql://root:motdepasse@localhost/sbe")



# # attach the data frame to the sql
# df_test.to_sql(name='structure', con=engine, if_exists='append', index=False)

