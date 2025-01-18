#If else in python.....

b=12
if 5<2:
    print("five is greater")
elif b==5:
    print("B=5")
else:
    print("b is greater",b)


#switch cases........

choice = int(input("Choice: "))

match choice:
    case 0:
        print("You chose zero")
    case 1:
        print("You chose one")
    case 2:
        print("You chose two")
    case default:
        print("default choice")

#operators AND OR NOT....

a = 5
b = 7
c = 9

if a > 4 and b > 6 and c > 8:
    print("All conditions are true")
    
elif a > 4 or b == 6 or c >= 8:
    print("At least one condition is true")

elif not(a > 4 and b > 6 and c > 8):
    print("At least one condition is false")