myset = {10, 20 , 30 ,40, 50, 50}
for x in myset:
   print(x)
#this will get all the values.
20 in myset
#this will  return true if the value is in the set.
#to add a value in a set
print(myset.add('edureka'))
#to add multiple values in a list
myset.update([ 10, 20, 30, 40, 50])
#to remove an item from a set
print(myset.remove('edureka'))
#we can use the discard or pop method to remove an item from a set as well.
myset = {10, 20, 30}
myset1 = {10,30,50}
print(myset.issubset(myset1))
#this will return false
print(myset.union(myset1))
#this will return a set with the union of the two sets.
# clear()	clears the items from a set
# copy()	returns the copy of the set
# difference()	returns a set with the difference of the two sets
# isdisjoint()	returns if the sets have intersection
# issubset()	returns if the set is a subset
# symmetricdifference()	returns a set with the symmetric difference
# update()	update the sets with union of the set