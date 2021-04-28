import json
a=["neelam","programer","24","24000",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"] 
e=["name","Designation","Age","salary"] 
i=0
dic1={}
dic2={}
dic3={}
dic4={}
f={}
while i<len(a):
    j=0
    while j<len(a):
        dic1[e[i]]=a[j]
        dic2[e[i]]=b[j]
        dic3[e[i]]=c[j]
        dic4[e[i]]=d[j]
        j=j+1
    f["emp1"]=dic1
    f["emp2"]=dic2
    f["emp3"]=dic3
    f["emp4"]=dic4
    i=i+1
# print(f)

data=json.dumps(f,indent=4)
print(data)
    




    

# a=[1,2,3,4,5,"kabita"]
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     i=i+1
# print(b)
    






