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

