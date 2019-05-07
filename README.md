# Craglist Scrapper

This is my scrapper.

Basically it will do the following.

From the cl_url.txt turn the urls into a json object.

For example

alburn = {
    "type1":"https://auburn.craigslist.org/d/art-media-design/search/med",
    "type2":"https://auburn.craigslist.org/d/web-html-info-design/search/web",
    "type3":"https://auburn.craigslist.org/d/computer-gigs/search/cpg",
    "type4":"https://auburn.craigslist.org/d/creative-gigs/search/crg"
}

Basically something like this for every city in America.

    all.text

Now we will use BeautifulSoup4, which is a Python dependency that allows for easy web scraping functionality.

So we will look for postings that are current.

For example today is 5/6 or May 6th.

So the scrapper will look at the first type object.

    "type1":"https://auburn.craigslist org/d/art-media-design/search/med",

In the html page, the posts are ordered by date.

So all the posts that have the date: May 6th will be scrapped into a csv formatted file. 

As you can image there will be quite a lot of posts that are posted on Craiglist for every city in America.

As so after this file is created.

First we will search for duplicate posts and remove them.

After that we will run a filter that searches for specific keywords.

    filter.py

After the file is put through these methods, there will be a file that has leads that are specific and relevent as well as being very current.

From there you can start pulling out emails to start the email campaign.

The important thing to remember is to treat each posting like a potential client. 

So we will add them to the CRM, and starting with follow ups, etc.

I think running this script 24/7 is the most efficent way to get these leads but it could use alot of bandwidth. 

So to start out with might just be a better idea to just run this scrapper early morning and late afternoon/evening. 

Also important to note to use a VPN.