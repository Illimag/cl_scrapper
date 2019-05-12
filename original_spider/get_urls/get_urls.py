# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
from bs4 import BeautifulSoup as soup
import time

from ghost import Ghost

ghost = Ghost()

with ghost.start() as session:
    # This needs to be randomized.
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}

    r = requests.get("https://www.craigslist.org/about/sites")
    content = soup(r.content, "html.parser")

    linksArray = []
    pathArray = [
        "search/cpg?is_paid=all&postedToday=1", # Gigs Computer gigs
        "search/crg?is_paid=all&postedToday=1", # Gigs Creative gigs
        "search/web?postedToday=1", # jobs Web Design
        "search/med?postedToday=1", # jobs Media
        "search/sof?postedToday=1", # jobs Software
        "search/sad?postedToday=1", # jobs System/Networking
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

