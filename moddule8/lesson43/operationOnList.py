mylist=['Appel','Banana','Pinappal','Strawberry','Watermellon']
print("lenght of list is ",len(mylist))
print("first element is ",mylist[0])

mylist.append('papaya')
print("updated list is ",mylist)

mylist.remove('Banana')
print("updated list is ",mylist)

mylist.sort()
print("sorted list is ",mylist)

mylist.reverse()
print("reversed list is ",mylist)

mylist.pop(1)
print("updated list is ",mylist)

mylist=mylist[1:3]
print("sliced list is ",mylist)

mylist.clear()
print("updated list is ",mylist)