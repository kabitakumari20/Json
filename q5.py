# import json
# def is_complex_num(objct):
#     if '__complex__' in objct:
#         return complex(objct['real'], objct['img'])
#     return objct

# complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
# simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
# print("Complex_object: ",complex_object)
# print("Without complex object: ",simple_object)


d={"num":"True","false":False,2:"two",3:"three","a":[1,2,3,4]}
import json
a=json.dumps(d)
print(a)
print(type(a))

