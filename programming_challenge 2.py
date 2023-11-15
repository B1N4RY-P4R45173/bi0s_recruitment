arr = input("Enter the numbers with spaces: ")
k = int(input("Enter the value of k: "))
def set_elements_to_zero(arr, start_index, end_index):
    for i in range(start_index, end_index):
        if arr[i] != 1:
            arr[i] = 2
split_arr = arr.split()
nums = [int(num) for num in split_arr]
indices = [index for index, value in enumerate(nums) if value == 1]
checkers = k - 1
#print (indices)
for i in indices:
        left = i - checkers
        right = i + checkers
        if left >= 0:
            twos = nums[left]
            set_elements_to_zero(nums, left, i)
        elif left < 0:
            left = 0
            set_elements_to_zero(nums, left, i)
        if right < len(nums):
            twos = nums[right]
            set_elements_to_zero(nums, i, right)
        elif right > len(nums):
            right = len(nums) -1
#print (nums)
if 0 in nums:
    zeros = nums.index(0)
    print ("-1, because water cannot be supplied to island", zeros + 1)
else:
    counters = k + checkers
    if len(nums) % counters ==0:
        plants = len(nums) / counters
    else:
        plants = (len(nums) // counters) + 1
    print ("This can effectively achieved by installing", plants, "desalination plant(s)")
