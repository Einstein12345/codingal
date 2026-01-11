mydict={'name':'Einstein','age':11}
print(mydict['name'])
print(mydict['age'])
mydict['age']=12
print(mydict)

mydict['grade']=5
print(mydict)

mydict.pop('age')
print(mydict)

mydict.clear()
print(mydict)