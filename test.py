# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup

# Specifiy the url
test_page = 'https://auburn.craigslist.org/d/computer-gigs/search/cpg'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(test_page)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

full_date = soup.find("time", {"class":"result-date"})
date = full_date.text
print date