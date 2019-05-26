# encoding=utf8

import json

# keywords are not cap sensitive. lower case w in "web" will also look for upper case "Web" and vice versa.
keywords = ["web", "Cloud", "Desktop","Mobile","Tablet","Server","Router","Switch","Embedded","Software","Hardware","Engineer","Architect","Scientist","Programmer","Developer","Branding","Graphics","UI","UX","Designer","IoT","Wearable","Technologies","Technologies","Scalable",
"Databases", "Data","Datacenter","computing","Networking","Innovation","Creativity","Social","Media","SEO","ASO","SEM","SMM","Object-Oriented","Procedural","Functional","Programming", "design", "designer", "website", "portfolio", "logo", "poster", "flyer", "ecommerce",
]

leads_with_keywords = {}
current_lead_number = 0
current_url_number = 0

with open("../test_run/data.json", 'r') as json_file:
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
                #print url
                this_url = url["url"]
                #print this_url
                leads_with_keywords[current_url_number] = []

                leads_with_keywords[current_url_number].append({'url':this_url})
                current_url_number+=1
                break

        current_lead_number+=1
with open('urls.json', 'w') as outfile:  
    json.dump(leads_with_keywords, outfile)
exit