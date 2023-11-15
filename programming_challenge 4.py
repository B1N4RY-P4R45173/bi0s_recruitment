user_input = input("Enter numbers separated by spaces: ")
input_list = user_input.split()
print (input_list)

sum = 0
for i, j in enumerate(input_list):
    #print (i , j)
    if int(j) > 0:
        sum += i

print(sum)
"""
"""
user_input = input("Enter numbers separated by spaces: ")
input_list = user_input.split()

sum_except_last = 0
no_of_zeros = 0

for i in input_list[:-1]: #because the last one is the deepest chamber
    num = int(i) 
    sum_except_last += num
    if num == 0:
        no_of_zeros += 1

sum_except_last += no_of_zeros

print(sum_except_last)
