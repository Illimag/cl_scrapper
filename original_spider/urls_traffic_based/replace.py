#!/usr/bin/python

for current_url in open("LT_Urls.txt"):

    str = current_url

    if "search/cpg?is_paid=all&postedToday=1" in current_url:
        replaced_url = str.replace("search/cpg?is_paid=all&postedToday=1", "d/computer-gigs/search/cpg")
        strip_string = replaced_url.rstrip('\r\n')
        print strip_string
    elif "search/crg?is_paid=all&postedToday=1" in current_url:
        replaced_url = str.replace("search/crg?is_paid=all&postedToday=1", "d/creative-gigs/search/crg")
        strip_string = replaced_url.rstrip('\r\n')
        print strip_string
    elif "search/web?postedToday=1" in current_url:
        replaced_url = str.replace("search/web?postedToday=1", "d/web-html-info-design/search/web")
        strip_string = replaced_url.rstrip('\r\n')
        print strip_string
    elif "search/med?postedToday=1" in current_url:
        replaced_url = str.replace("search/med?postedToday=1", "d/art-media-design/search/med")
        strip_string = replaced_url.rstrip('\r\n')
        print strip_string
    elif "search/sof?postedToday=1" in current_url:
        replaced_url = str.replace("search/sof?postedToday=1", "d/software-qa-dba-etc/search/sof")
        strip_string = replaced_url.rstrip('\r\n')
        print strip_string
    elif "search/sad?postedToday=1" in current_url:
        replaced_url = str.replace("search/sad?postedToday=1", "d/systems-networking/search/sad")
        strip_string = replaced_url.rstrip('\r\n')
        print strip_string