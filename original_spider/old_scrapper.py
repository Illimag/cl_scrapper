# This actually just gets all the urls.

import requests
from bs4 import BeautifulSoup as soup

r = requests.get("https://www.craigslist.org/about/sites")
content = soup(r.content, "html.parser")

linksArray = []
pathArray = [
    "search/cpg?is_paid=all&postedToday=1", # Gigs Computer gigs
    "search/crg?is_paid=all&postedToday=1", # Gigs Creative gigs
    "search/web?postedToday=1", # jobs Web Design
    "search/med?postedToday=1", # jobs Media
    "search/sof?postedToday=1", # jobs Software
    "search/sad?postedToday=1" # jobs System/Networking
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

i = 0
for link in linksArray:
    for path in pathArray:
        search = (link + path)
        print search
