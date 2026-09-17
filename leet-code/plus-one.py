# Plus One
# Link: https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits):

        num = ""

        # loop through 
        for i in range(len(digits)):
            num = num + str(digits[i])

        num = int(num)+1

        arr = [int(i) for i in str(num)]

        print(arr)




sol = Solution()

digits = [4,3,2,1]

sol.plusOne(digits)