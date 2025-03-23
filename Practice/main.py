# File I/O
with open("test.txt") as f:
    for line in f:
        print(line.strip())

# JSON
import json
profile = '{"name": "David Ng"}'
obj = json.loads(profile)
print(obj["name"])

#Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't devide by zero")
finally:
    print("Done")

#List 
squares = [x * x for x in range(5)]
print(squares)