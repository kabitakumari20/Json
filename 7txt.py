import json
dic={}
with open("name.txt") as f:
    for line in f:
        key,value=line.strip().split(None,1)
        dic[key]=value.strip()
file=open("que7.json","w")
json.dump(dic,file,indent=4)
print(json.dumps(dic,indent=4))
file.close()
