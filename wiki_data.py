
import urllib.request as re
import urllib.error as er

from bs4 import BeautifulSoup
import ssl

context=ssl._create_unverified_context()
site="https://en.wikipedia.org/wiki/"
print("enter search query:")
search=input()
site_new=site+search
try:

    page=re.urlopen(site_new,context=context)

    soup=BeautifulSoup(page,"html.parser")
    #print(soup.get_text)


    stuff=soup.find('div',attrs={"class":"mw-content-ltr"}).find_all('p')
    for element in stuff:

        print(element.text)
        print(" ")
        print(" ")

except er.HTTPError as er1:
    print("no result")




