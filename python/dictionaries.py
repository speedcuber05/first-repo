dic= {'brand': 'ford', 'release':1947,'price':4500 }
print(dic)
x=dic.get('brand')
print(x)
dic['colour']='blue'   #you can also update a value with this
keys = dic.keys()
print(keys)
values = dic.values()
print(values)
item = dic.items()    #gives a list of a tuple pairs with the key and their value
print(item)
for i in dic:      #print all the keys
    print(i)
for j in dic:
    print(dic[j])  #print all the values
dic.update({"year": 2020})
print(dic.pop('release'))