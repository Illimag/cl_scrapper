import json
















current_lead_number = 0
current_url_number = 0

with open("incoming/lead.json", 'r') as json_file:
    data = json.load(json_file)
    total_number_of_items_in_data = len(data)

    for x in range(0, total_number_of_items_in_data):
        turn_into_string = str(current_lead_number)
        lead = (data[turn_into_string])
        url = lead[1]
        text_in_url = url["url"]

        print text_in_url
        current_lead_number+=1

        





with open("master.json",'r') as master_json:
    master = json.load(master_json)

