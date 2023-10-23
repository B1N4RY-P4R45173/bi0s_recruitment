k = int(input("enter a number: ")) 
user_input = input("enter the numbers with space in between: ") 
input_list = user_input.split() 
input_list = [int(x) for x in input_list] 
arr = input_list 
element_to_count = 1 
count = arr.count(element_to_count) 
 
try: 
    for i in range (len(arr)): 
        if arr[i] == 0: 
            if arr[i - 2] == 1 or arr[i + 2] ==1: 
                c =1 
            else: 
                c = -1 
except Exception as e: 
    c = -1 
if k > (count): 
    c = 1 
if c == 1:  
    print("1") 
elif c == -1: 
    print ("-1") 
else: 
    print ("idk what's happening")
