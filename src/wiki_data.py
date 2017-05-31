
import urllib.request as re
import urllib.error as er
import sys


from bs4 import BeautifulSoup
import ssl

sys.tracebacklimit= None

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"


context=ssl._create_unverified_context()
site="https://en.wikipedia.org/wiki/"

try:
    if len(sys.argv)>2:
        raise Exception("too many arguments usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")
    site_new=site+sys.argv[1]




    page=re.urlopen(site_new,context=context)

    soup=BeautifulSoup(page,"html.parser")
    #print(soup.get_text)



    tag_head=['h1','h2','h3','h4','h5','h6']
    tag_para=['p']

    tags= soup.findAll()
    for tag in tags:
        if tag.name in tag_head:
            if tag.text=='References':
                break
            else:
                print(OKBLUE+tag.text+ENDC)
        elif tag.name in tag_para:
            print(tag.text)
        else:
            continue

    for tag in tags:
        if tag.name in tag_head:
            print(tag.text)


except er.HTTPError as er1:
    print("no result")
except IndexError:
    print("usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")





