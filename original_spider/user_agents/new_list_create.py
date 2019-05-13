# This is a script that scrapes all the user agents from this URL
# https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/

# I keep getting blocked make sure to always have delays as well as using a VPN when scraping.

import requests
from bs4 import BeautifulSoup as soup
import time

links =[
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/1",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/2",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/3",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/4",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/5",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/6",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/7",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/8",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/9",
    "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/10"
]

for link in links:

    r = requests.get(link)

    content = soup(r.content, "html.parser")
    time.sleep(5)
    test = content.find_all("div")

    print test