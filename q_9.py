# .9 Apki pass ek shopping name ki ek dictionary hai Apki dictionary ka use kar ke ek json file create karna hai. Aur apko kuch task perform karne hai jaise ki 1. main dekhna chahta hu shopping list ko json file dekhna.

# phir main user se poochu ga ki kon sa item khareedna chahte ho.

# uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.

# phir aapka wo number of items json file se remove karna hai.

# Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.
# a={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",} }

import json
a={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",} }
item=input("enter the items=")
user1=int(input("enter the num="))
c=a["shopping_list"][item]
rem=int(c)-user1
a["shopping_list"][item]=rem
print(a)
b=json.dumps(a)
print(b)


