class ValueOnPos:
    def insert(self,nums, index, value):
        nums.append(None)
        for i in range(len(nums) - 2, index - 1 , -1):
            nums[i + 1] = nums[i]
        nums[index] = value

        print(nums)

a = ValueOnPos()
nums = [11,22,33,44,55,66,77,88,99,1010,1111,1212]
a.insert(nums, 2 , 69)