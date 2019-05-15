# CraigScraper.py
# This is my web spider that scrapes Craiglist for leads.
# It works in several parts.
# 1. Get a text file with all the CL URLS that are written to search each city, specific category, then filter only for today.
# 2. Get a list of User Agents as text file then randomly selects one and makes it the header for the get request.
# 3. Using a rotating proxy service with each HTTP request, the IP is changed for each request.
# 4. The get request recieves the full html of the URL.
# 5. Then we have a method to see if there are no postings, if so then go to next URL.
# 6. If there are postings we see if they are nearby which are duplicate postings, if so go to next URL.
# 7. Then it will print out the href and title of every city on Craiglist.

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests

from bs4 import BeautifulSoup as soup

import time

import random

loop = True

if loop:

    i = 0
    # all_today.txt is a list of all the today files.
    # To get an updated all_today.txt run the get_urls/get_urls.py
    for current_url in open("urls/all_today2.txt"):
            # Current URL that the spider is searching through

            # Rotate User Agents
            with open("user_agents/user_agents.txt") as f:
                lines = f.readlines()
                line = random.choice(lines)
                user_agent = line.rstrip('\r\n')
            headers = {'User-Agent': user_agent, 'Content-Type': 'application/x-www-form-urlencoded'}

            # Proxy List
            http_proxy  = "http://83.149.70.159:13042"
            https_proxy = "http://83.149.70.159:13042"
            ftp_proxy   = "ftp://83.149.70.159:13042"
            proxyDict = { 
                        "http"  : http_proxy, 
                        "https" : https_proxy, 
                        "ftp"   : ftp_proxy
                        }

            # So Cragslist won't block IP
            time.sleep(1)

            # This is the request for Craiglists behind a rotating user agent header and proxy.
            for i in range(100):
                try:
                    search = requests.get(current_url,headers=headers,proxies=proxyDict)
                    print(i)
                except:
                    print(i)
            else:
                print("failed")
                sys.exit(1)

            # So Cragslist won't block IP
            time.sleep(1)

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

                        exit # Exit loop and look at next post in table
                    else:

                        # No nearby tag in current post of table 
                        print("notest1")
                        print current_url
                        print post.find("a", {"class":"result-title hdrlnk"})

                        print('\n')


    print "Total output =", i, ""