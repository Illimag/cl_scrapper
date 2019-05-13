
import requests
import random

# This is where the user agents need to be rotated
with open("../user_agents/user_agents_list0.txt") as f:
    lines = f.readlines()
    line = random.choice(lines)
    user_agent = line.rstrip('\r\n')
url = 'https://httpbin.org/user-agent'
headers = {'User-Agent': user_agent}
# print headers
response = requests.get(url,headers=headers)

html = response.content
print(response.content)
