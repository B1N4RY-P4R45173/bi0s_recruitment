X = input("enter the string: ")
Y = int(input("enter the number of times you wanna swap: "))
lst = sorted(X)

differences = 0
for i in range(len(X)):
    if X[i] != lst[i]:
        differences += 1
        
if 2*Y >= differences:
    print ("YES")
else:
    print ("NO")
