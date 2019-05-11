# CraigScraper.py
#
# ddm
#       2017 -- Fixing text issues.
#           Fixed - Was not checking for whole words - Any C triggered a match
#           Fixed - Matches were case sensitive.
#           Fixed - Was printing a copy for every keyword that matched.
#           Added Rejection Words
# ddm

# jaemnkm
#       2019 -- Updated parts of code
#           Changed pathArray so only post from today
#           Imported time module
#           Added time.sleep()
#
# jaemnkm

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

    # This is the first user agent that is sent while doing a request.get
    url = 'https://httpbin.org/user-agent'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(url,headers=headers)

    html = response.content
    print(response.content)

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

    i = 0
    for link in linksArray:
        for path in pathArray:
            # Current URL that the spider is searching through
            current_url = link + path

            # This is where the userr agents need to be rotated
            url = 'https://httpbin.org/user-agent'
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            headers = {'User-Agent': user_agent}
            response = requests.get(url,headers=headers)

            html = response.content
            print(response.content)

            search = requests.get(current_url)
            # s_content is the full html page of the current URL.
            s_content = soup(search.content, "html.parser")
            # This looks for the nothing found alert. If it finds it in the HTML.
            # Then it means there are no results so the program will exit.
            # It then goes to the next url to do a search.
            zero_results = s_content.find("div", {"class":"alert alert-sm alert-warning"})
            if zero_results:

                # If there are no results
                print("test")
                print current_url

                # So Cragslist won't block IP
                time.sleep(5)
                exit # Exit the current loop and goes to next URL
            # This will reduce the number of duplicate posts
            else:

                # If there are results
                print("notest")
                print current_url

                # table is the full list of posts on the current url html page
                table = s_content.find_all("li", attrs={'class': "result-row"})

                # Now we iterate through all the posts in the table
                for post in table:

                    # In the current post of the table if there is a specific tag
                    # <span class="nearby"></span>
                    # Then this is a duplicate posting.
                    nearby_results = post.find("span", {"class":"nearby"})
                    if nearby_results:

                        # If there are nearby results posts which are duplcates
                        print("test1")
                        print current_url
                        # print post

                        # So Cragslist won't block IP
                        time.sleep(5)
                        exit # Exit loop and look at next post in table
                    else:

                        # No nearby tag in current post of table 
                        print("notest1")
                        print current_url
                        print post.find("a", {"class":"result-title hdrlnk"})

                        # So Cragslist won't block IP
                        time.sleep(10)

                        print('\n')


    print "Total output =", i, ""