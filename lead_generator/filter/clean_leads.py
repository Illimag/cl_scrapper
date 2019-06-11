# encoding=utf8
import json
import time
from ftplib import FTP_TLS
import os

# keywords are not cap sensitive. lower case w in "web" will also look for upper case "Web" and vice versa.
keywords = ["web", "Cloud", "Desktop","Mobile","Tablet","Server","Router","Switch","Embedded","Software","Hardware","Engineer","Architect","Scientist","Programmer","Developer","Branding","Graphics","UI","UX","Designer","IoT","Wearable","Technologies","Technologies","Scalable",
"Databases", "Data","Datacenter","computing","Networking","Innovation","Creativity","Social","Media","SEO","ASO","SEM","SMM","Object-Oriented","Procedural","Functional","Programming", "design", "designer", "website", "portfolio", "logo", "poster", "flyer", "ecommerce",
]

leads_with_keywords = {}
current_lead_number = 0
current_url_number = 0

# Watchdog runs the clean_leads.py with os.system.
# Because the run_watchdog.py file is located in test_leads
# When clean_leads.py is run
# All files paths are relative to the run_watchdog.py file.



with open("lead.json", 'r') as json_file:
    data = json.load(json_file)
    total_number_of_items_in_data = len(data)
    #print total_number_of_items_in_data
    #print data
    for x in range(0, total_number_of_items_in_data):
        turn_into_string = str(current_lead_number)
        lead = (data[turn_into_string])
        #print lead
        title = lead[0]
        #print title
        text_in_title = title["title"]

        for keyword in keywords:
            if keyword in text_in_title:
                lead = (data[turn_into_string])
                #print lead
                url = lead[1]
                title = lead[0]
                #print url
                this_title = title["title"]
                this_url = url["url"]
                #print this_url
                leads_with_keywords[current_url_number] = []

                leads_with_keywords[current_url_number].append({'title':this_title})
                leads_with_keywords[current_url_number].append({'url':this_url})
                current_url_number+=1
                break

        current_lead_number+=1
with open('out_lead.json', 'w') as outfile:  
    json.dump(leads_with_keywords, outfile)
exit

ftp=FTP_TLS()
ftp.set_debuglevel(2)
ftp.connect('192.168.0.109', 36891)
ftp.sendcmd("USER spider_user")
ftp.sendcmd("PASS test")
file = open('out_lead.json','rb')     
ftp.storbinary('STOR out_lead.json', file) 
file.close()  
ftp.close()


os.remove("lead.json")
os.remove("out_lead.json")

# Because another file is created which is out_lead.json
# Watchdog runs the clean_leads script again.
# But because there is no lead.json because spider.py hasen't
# It throws a missing file error.
# Currently this is fine for now.
# But eventually a solution should be for Watchdog to watch 
# For specific file.
