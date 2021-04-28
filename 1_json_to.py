# Json data ko python object main convert karne ka program likho?.
import json
with open("python.json","r") as f:
    a=json.load(f)
    print(a)
    print(type(a))


