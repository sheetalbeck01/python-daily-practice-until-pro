# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
#
# Given:
# - A list of integers called nums
# - An integer called target
#
# Task:
# Find two different elements in nums whose sum is equal to target.
#
# Return:
# Return the indices of those two elements.
#
# Rules:
# - You cannot use the same element twice.
# - Exactly one valid solution will exist.
# - The answer can be returned in any order.
#
# Example:
# nums = [2, 7, 11, 15]
# target = 9
#
# nums[0] + nums[1] = 2 + 7 = 9
#
# Output:
# [0, 1]
#
# Constraints:
# - nums will contain at least 2 elements.
# - nums can contain up to 10,000 elements.
# - Numbers and target can be negative, zero, or positive.
#
# Follow-up:
# Try to find a solution faster than O(n^2).


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j]:
                    return [i,j]

solution = Solution()

print(solution.twoSum([2,7,11,15], 9))