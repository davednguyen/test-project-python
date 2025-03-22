# File I/O
with open("test.txt") as f:
    for line in f:
        print(line.strip())

# JSON
import json
profile = '{"name": "David Ng"}'
obj = json.loads(profile)
print(obj["name"])

#Requests Library (for API Calls)
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())