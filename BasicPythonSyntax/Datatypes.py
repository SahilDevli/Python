#int
i=1
print(i)

#str
stng = "str data type"
print(stng)

#float
f=1.03456
print(f)

# bool
b = False
print(b)

#complex
com = 9j
print(com)

# None
n = None
print(n)


#list -> mutable (can be changed after they are created)
list1 = [1,2,3,4,5,6,7]
list2 = ["a12", "bcx", "cff", "d"]
list3 = ["a12", 5.04, True, "d"]

list1[2] = 100j
print (list1)

#tuple -> immutable (can't be changed after they are created)
tuple1 = (1,2,3,4,5)
tuple2 = ("hello", "world", "w")
tuple4 = ("hello", 1.002, True)
# tuple1[3] = 100000
print (tuple1, tuple2, tuple4)

#dictionary -> mutable -> key and value pairs
dic1 = {"key": "value","name" : "xyz","integer" : 123}
print("\ndictionary:-")
for i in dic1:
    print(i,":",dic1[i])

print("\n")


#range ->  (0 to n) or (n to n)
r = range(7)
r1 = range(4,8)
print (r)
print (r1)

# set
set = {"apple", "banana", "cherry"}
set2 = {90.99,True,1}
print(set)

# frozenset
fs = frozenset({"apple", "banana", "cherry"})
print(fs)