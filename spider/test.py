# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup

# Specifiy the url
test_page = 'https://dothan.craigslist.org/search/cpg?is_paid=all&postedToday=1'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(test_page)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# This looks for the nothing found alert. If it finds it in the HTML
# Then it means there are no results so the program will exit.
# It should go to the next url to do a search.
zero_results = soup.find("div", {"class":"alert alert-sm alert-warning"})
if zero_results:
    exit
else:
    table = soup.find("ul",{"class":"rows"})


for row in rows:
    print rows

resultsArray = []

resultsArray = soup.find_all("time", {"class":"result-date"})

print resultsArray



# if date == "May  1":
#     print "true"
# else:
#     print "false"