class Solution:
        def singleNonDuplicate(self, nums):
            t = nums[0]
            for i in range(1, len(nums)):
                t = t ^ nums[i]
            return t