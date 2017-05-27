
import urllib.request as re
import urllib.error as er
import sys


from bs4 import BeautifulSoup
import ssl

sys.tracebacklimit= None

context=ssl._create_unverified_context()
site="https://en.wikipedia.org/wiki/"

try:
    if len(sys.argv)>2:
        raise Exception("too many arguments usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")
    site_new=site+sys.argv[1]




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
except IndexError:
    print("usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")





