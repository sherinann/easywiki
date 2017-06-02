
import urllib.request as re
import urllib.error as er



from bs4 import BeautifulSoup
import ssl

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

tag_head = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
tag_para = ['p', 'li']



context=ssl._create_unverified_context()



def getSpecialResult(searchSpecialBeg,searchSpecialEnd,searchItem):

    searchQuery=searchItem.replace(" ", "+")
    site_new=searchSpecialBeg+searchQuery+searchSpecialEnd
    page = re.urlopen(site_new, context=context)

    soup = BeautifulSoup(page, "html.parser")
    #print(soup.get_text)

    for tags in soup.find(name='div',attrs={"class":"mw-search-result-heading"}).findAll('a'):

           # print(tags.text)
            return tags.text



def getResult(site,searchItem):


    site_new = site + searchItem

    try:
        page = re.urlopen(site_new, context=context)

        soup = BeautifulSoup(page, "html.parser")
        #print(soup.get_text)


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
        return 1

    except er.HTTPError as er1:
        return 0








