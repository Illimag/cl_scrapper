

import requests
from bs4 import BeautifulSoup as soup

r = requests.get("https://www.craigslist.org/about/sites")
content = soup(r.content, "html.parser")

linksArray = []
pathArray = [
    "d/computer-gigs/search/cpg",
    "d/creative-gigs/search/crg",
    "d/art-media-design/search/med",
    "d/internet-engineering/search/eng",
    "d/software-qa-dba-etc/search/sof",
    "d/systems-networking/search/sad",
    "d/web-html-info-design/search/web"
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
