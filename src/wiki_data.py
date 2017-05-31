
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
searchQuery=""

context=ssl._create_unverified_context()
siteDefault="https://en.wikipedia.org/wiki/"

search="https://en.wikipedia.org/w/index.php?search="+searchQuery+"&amp;title=Special%3ASearch&amp;fulltext=1"


def getSpecialResult(search):
    page = re.urlopen(search, context=context)

    soup = BeautifulSoup(page, "html.parser")
    print(soup.get_text)


def getResult(site,searchItem):

    site_new = site + searchItem

    page = re.urlopen(site_new, context=context)

    soup = BeautifulSoup(page, "html.parser")
    print(soup.get_text)

    tag_head = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    tag_para = ['p', 'li']

    tags = soup.findAll()
    for tag in tags:
        if tag.name in tag_head:
            if tag.text == 'References' or tag.text == 'Navigation menu':
                break
            else:
                print(OKBLUE + tag.text + ENDC)
        elif tag.name in tag_para:
            print(tag.text)
        else:
            continue




if __name__=="__main__":
    try:

        if len(sys.argv) > 2:
            raise Exception( "too many arguments usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")
        else:
            site=siteDefault
            searchItem=sys.argv[1]
            getResult(site,searchItem)



    except IndexError:
        print("usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")
    except er.HTTPError as er1:
        for i in sys.argv[1]:
            if i == " ":
                i = '+'
        searchQuery=sys.argv[1]
        getSpecialResult(search)

