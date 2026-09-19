
# This is my brute force code
# Got time limit in leetcode

nums = [1,2,3,1]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            print(nums[i],nums[j])


# My version

nums = [1,2,3,4,5]

num_length = len(nums)

set1 = set(nums)

new_length = len(set1)

if num_length != new_length:
    print("found")


# Found this solution also in leet code using loop and its the best optimized solution. 
nums = [1,2,3,4,5]

num_set = set()
for n in nums:
    if n in num_set:
        print('Found')
    num_set.add(n)