# Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array


class Solution:
    def remove_duplicates(self, nums):
        temp = nums[0]
        unique = [nums[0]]
        for i in range(1, len(nums)):
            if temp != nums[i]:
                unique.append(nums[i])
                temp = nums[i]


        return unique
            

sol = Solution()

print(sol.remove_duplicates([1,1,1,1,1,1,3,5,7,8,8,8,9]))

# -------------------------------------------------------
# but this solution is creating new list without duplicates but in leetcode I've to rearrange nums
class SolutionLeet:
    def remove_duplicates(self, nums):
        temp = nums[0]
        unique = [nums[0]]
        for i in range(1, len(nums)):
            if temp != nums[i]:
                unique.append(nums[i])
                temp = nums[i]

        k = len(unique)        
        print(k, "nums=", unique)
            

sol2 = SolutionLeet()

sol2.remove_duplicates([0,0,1,1,1,2,2,3,3,4])

# # -------------------------------------------------------
# I've to rearrange the orignal nums according to leetcode question
# Doing here in short wihout class first

num1 = [0,0,1,1,1,2,2,3,3,4]
first = num1[0]
index = 1
for i in range(1, len(num1)):
    if num1[i] != first:
        num1[index] = num1[i]
        first = num1[i]
        index += 1

print("NUM:" , num1)

