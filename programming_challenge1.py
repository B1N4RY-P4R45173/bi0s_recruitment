user_input = input ("enter the numbers with spaces: ").split()
arr =[]
for i in user_input:
    arr.append(int(i))
count = 0
seen = set()
# prints same array (for checking if the array is correct)
print (arr)
while True:
    max_val = max(arr)
    min_val = min(arr)
    if max_val ==0:
        break #max_val will be 0 only if all elements in the array are 0, hence if max_val = 0 it will break the loop
    max_index = arr.index(max_val)
    arr[max_index] = min_val
    count = count + 1
    print (arr)
    for i in range(len(arr)):
        if arr[i] in seen and arr[i] !=0: #checks if the elements are repeated already, and also makes sure that if the element is 0 it doesnot check for anything else. This line is imp bcz if the array becomes like [1, 0, 0] it should not change the 0 into 0 and count it as another step. 
            arr[i] = 0
            count = count + 1
            print (arr)
        else:
            seen.add(arr[i])
print (count)
