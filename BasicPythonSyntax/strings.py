# strings in python...


#slice - s[index1 : index2]

s = "Hello World!"
print(s[-5:-2])

#concatenate - str1 + str2

st1 = "Hello"
st2 = "World!"
st3 = st1 + st2
print(st3)

#Format - "f" & {num}
age = 36
txt1 = f"My name is John, I am {age+1}"
txt2 = f"My name is John, I am {age+1:2f}"
txt3 = "My name is John, I am {age+1:2f}"
print(txt1)
print(txt2)


#reverse ........................................

def rev(strn):
    revStr = ""
    for i in range(len(strn)-1,-1,-1):
        revStr += strn[i]
    return revStr

var = input("Enter a string : ")
var2 = rev(var)
print(var2)