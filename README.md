# Craglist Scrapper

The scrapper currently does the following.

All the URLS are from Craiglist with only today listing selected.

So first if there are no listing then it will go to next URL.

If there is listing then it looks to see if it is a nearby type.

Nearby types are going to be a duplicate eventually so we remove it.

If it is not a nearby then we will print out the post.

# Current issue

Currrently I have run into a problem where Craiglist after maybe 300 URLS it does a temporary block to my IP address maybe even related to MAC Address. 

The temporary block is because of things such as not having a user agent.

So to solve this problem I will need to use a headless brower.

There will also need to be additional things added to the script to make it seem more like a human user.

For example things such as images not being downloaded, page resources not downloaded in normal order, Pages being downloade faster than a human can read them, cookies not being set properly. Also things like mouse movements not human like.

To start just having the headless browser to trick Craiglist into thinking it is a browser will be nessessary.

We can also try to fake a user agent for example here is a header field.

A good idea maybe to rotate my user agents and VPNS.

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
r = requests.get(url, headers=headers)
