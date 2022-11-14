import urllib.request
from bs4 import BeautifulSoup 
import re
import sys

linkArray = []
emailArray = []

def getemails(link):
    x = urllib.request.urlopen(link)
    soup = BeautifulSoup(x, features="html.parser")
    mailtos = soup.select('a[href^=mailto]')
    for i in mailtos:
        if i.string != None:
            emailAddr = i.string.encode('utf=8').strip().decode()
            if emailAddr not in emailArray:
                emailArray.append(emailAddr)
                print(f"Found email: {emailAddr}")
                

def getlinks(link):
    try:
        x = urllib.request.urlopen(link)
        soup = BeautifulSoup(x, features="html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            lnk = (link.get('href'))
            if lnk not in linkArray:
                linkArray.append(lnk)
                print(lnk)
                getemails(lnk)
                getlinks(lnk)
    except:
        print("================================")

if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    print("Usage: python3 harvestlinks.py <url>")
    exit(0)

try:
    getlinks(url)
except:
    KeyboardInterrupt


        

