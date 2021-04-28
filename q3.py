# Q.3 Python object ko json string mai convert karne ka program likho?
import json
a={2:"kabita",3:"three","four":"4"}
print(type(a))
f=open("my_name.json","w")
b=json.dump(a,f,indent=2)
print(b)