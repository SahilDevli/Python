list1 = [1,2,3,4,5,6,7]
list2 = ["a12", "bcx", "cff", "d"]
list3 = ["a12", 5.04, True, "d"]

#indexing & slicing..............................
print(list1[:4])

#condition...
if 1 in list1:
    print("Element found in list1")



#methods()......................................

#len()................................
lenAll = len(list1 + list2 + list3)
len1 = len(list1)
print ("Length of 1st list: ",len1)
print ("Sum of lenght of All lists: ",lenAll)

#type()................................
print (type(list1),type(list2),type(list3))

#constructor of list by using list((content/element))..............
listclass = list(("element1","element2","element3",1,2,3,True,False))
listclass.append(["ele","e","99"])
print (listclass)

#max() & min()..........................
print ("Max in list1: ",max(list1))
print ("Min in list1: ",min(list1))

#.index(element)...............................
print ("Index of 'a12' in list2: ",list2.index("a12"))

#count()..............................
print ("Count of 'a12' in list2: ",list2.count("a12"))

#insert()...............................
list2.insert(2, "inserted")
print (list2)

#remove()...............................
list2.remove("inserted")
print (list2)

#pop()...............................
print ("Popped element: ",list2.pop())
print (list2)

#extend()...............................
list2.extend(["e","e","99"])
print (list2)

#clear()...............................
list2.clear()
print (list2)

#copy()...............................
list4 = list1.copy()
list4.append("new")
print ("List1: ",list1)
print ("List4: ",list4)

#reverse()...............................
list1.reverse()
print ("Reversed list1: ",list1)

#sort()...............................
list1.sort()
print ("Sorted list1: ",list1)


#slicing...............................
print ("Slicing list1: ",list1[1:4])

#nested list...............................
list6 = [1,2,[3,4,[5,6]],7]
print ("Nested list: ",list6)

#nested list access...............................
print ("Nested list access: ",list6[2][1])

#nested list append...............................
list6[2].append(7)
print ("List after append: ",list6)

#nested list remove...............................
list6[2].remove(7)
print ("List after remove: ",list6)

#nested list sort...............................
list6[2].sort()
print ("List after sort: ",list6)

#nested list reverse...............................
list6[2].reverse()
print ("List after reverse: ",list6)

#nested list pop...............................
print ("Popped element from nested list: ",list6[2].pop())
print ("List after pop: ",list6)

#nested list copy...............................
list7 = list6[2].copy()
list7.append("new")
print ("Nested list1: ",list6[2])
print ("Nested list7: ",list7)

#nested list clear...............................
list6[2].clear()
print ("List after clear: ",list6[2])

#nested list extend...............................
list6[2].extend(["e","e","99"])
print ("List after extend: ",list6[2])
