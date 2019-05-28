import json
import csv

with open("urls.json", "r") as json_file: 
    data = json.load(json_file)
    total_number_of_items_in_data = len(data)
    array = []
    second_array = []
    current_lead_number = 0

    for x in range(0, total_number_of_items_in_data):
        turn_into_string = str(current_lead_number)

        lead = (data[turn_into_string])
        url = lead[0]
        this_url = url["url"]

        array.append(this_url)
        current_lead_number+=1

    a=list(set(array))

    for val in a:
        test = val.rstrip('\r\n')
        test_string = ([test])

        second_array.append(test_string)
        
        with open('output.csv','wb') as f:
            writer = csv.writer(f,delimiter =' ',quotechar ='|',quoting=csv.QUOTE_NONE)
            writer.writerow(['email'])
            writer.writerows(second_array)