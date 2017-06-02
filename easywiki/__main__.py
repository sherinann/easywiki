
import ssl
import sys
from easywiki import wiki_data

sys.tracebacklimit= None



siteDefault="https://en.wikipedia.org/wiki/"

searchSpecialBeg="https://en.wikipedia.org/w/index.php?search="
searchSpecialEnd="&amp;title=Special%3ASearch&amp;fulltext=1"

def main():
    try:
        if len(sys.argv) > 2:
            raise Exception(
                "too many arguments usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")
        else:
            searchItem = sys.argv[1]

            status = wiki_data.getResult(siteDefault, searchItem)
            if status == 0:
                key = wiki_data.getSpecialResult(searchSpecialBeg, searchSpecialEnd, searchItem)
                wiki_data.getResult(siteDefault, key)



    except IndexError:
        print("usage: wiki_data.py <arg1> \n[use \" \" to enclose argument with spaces]")

if __name__ == '__main__':
    main()