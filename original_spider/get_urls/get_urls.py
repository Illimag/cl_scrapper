# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
from bs4 import BeautifulSoup as soup
import time

#from ghost import Ghost

# ghost = Ghost()

# with ghost.start() as session:
    # This needs to be randomized.
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}

r = requests.get("https://www.craigslist.org/about/sites")
content = soup(r.content, "html.parser")

linksArray = []
pathArray = [
    "d/art-media-design/search/med", # Gigs Computer gigs
    "d/software-qa-dba-etc/search/sof", # Gigs Creative gigs
    "d/systems-networking/search/sad", # jobs Web Design
    "d/technical-support/search/tch", # jobs Media
    "d/web-html-info-design/search/web", # jobs Software
    "d/computer-gigs/search/cpg", # jobs System/Networking
    "d/creative-gigs/search/crg", # jobs System/Networking
]

print "\n"      # Two blank lines
loop = True
for country in content.find_all("div", attrs={'class': "colmask"}):
    if loop:
        for states_box in country.find_all("div"):
            # for state in country.find_all("h4"):
            #     print("-------------------------------------\n\n\n")
            #     print(state.text + "\n")
            #     print(state.next_sibling)

            for area in states_box.find_all("ul"):
                for location in area.find_all("a"):
                    linksArray.append(location.get("href"))

    loop = False
# ddm -- The above code is an odd way to only use the first item in the list...

for link in linksArray:
    for path in pathArray:
        url = link + path
        print url