# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka 
# program likho? Example: Input :- Output:- JSON data:
import json
a={'4': 5,'6': 7,'1': 3,'2': 4}
list1=[]
list2=[]
for key in a:
    list1.append(key)
    list2.append(a[key])
for i in range(0,len(list1)):
    for j in range(0,len(list1)):
        if list1[i]<list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
        if list2[i]<list2[j]:
            list2[i],list2[j]=list2[j],list2[i]
d={}
for l in range(0,len(list1)):
    d[list1[l]]=list2[l]
print(d)
with open("ques4.json","w") as json_ob:
    data=json.dump(d,json_ob)


# print(json.dumps(a, sort_keys=True, indent=4))
