mySet={1,2,2,3,4,4,4,4}
print("set ",mySet)

mySet.add(5)
print("updated set is ",mySet)

mySet2={2,4,4,6}
print("difference")
print(mySet.difference(mySet2))

print("symmeteric difference")
print(mySet.symmetric_difference(mySet2))