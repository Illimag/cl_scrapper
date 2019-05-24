import requests

from bs4 import BeautifulSoup as soup

url ="https://sfbay.craigslist.org/sfc/cpg/d/san-francisco-new-flexible-delivery/6891386620.html"

test = requests.get(url)

print test.text