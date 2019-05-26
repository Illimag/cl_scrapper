import json

with open("urls.json", "r") as json_file: 

    a=list(set(f))

    for val in a:
        test = val.rstrip('\r\n')
        print test