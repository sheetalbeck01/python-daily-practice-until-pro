# Find square root of a non negative integer and return the rounded down to the nearest integer.
# Do not use built-in exponent function or operator, pow(x, 0.5) in c++ or x ** 0.5 in python.
# Link: https://leetcode.com/problems/sqrtx/description/


class Solution:
    def mySqrt(self, x):
        i = 1
        answer = 0
        while i * i <= x:
            answer = i   
            i += 1
        return answer

sol = Solution()

print(sol.mySqrt(8))