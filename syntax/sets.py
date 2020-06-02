
#set creation
set1=set()

String = "AlamaKota"
set2 = set(String)
print(set2)
set3=set(["code", "for", "everyone"])
print(set3)

#how to add elements to set
set4=set([1,2,3,3,"Code",5,6,"String",7,8,9])
set4.add("Cat")
print(set4)
set4.update(set([0,0,0,0,10, 2, 8, 11, 13]))
print(set4)

set5=set([1,2,3,3,"Code"])
for i in set5:
    print(i, end=" ")

#how to delete sth from the set - you have to be sure that the element exist
set5.remove(2)
print(set5)

#discard - you can "delete" even the element that doesn't exist
set5.discard(9)
print(set5)

#pop - removes the first element from a set
set5.pop()
print(set5)

#clears the whole set
set1.clear()
print(set1)

#using set we can remove the duplicates from our list, because it removes them by itself
# to remove the duplicates we can throw the array to the set and then set back to array
# remeber!!! add() is for sets append() for arrays
a = [7, 7, 1,1, 9,6,5,8,9,4,3]
duplicate_items = set()
unique_items = []
for x in a:
    if x not in duplicate_items:
        unique_items.append(x)
        duplicate_items.add(x)
print(duplicate_items)
print(unique_items)
