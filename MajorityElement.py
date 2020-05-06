"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""
def majorityElement(nums):
    set1 = set(nums)
    res = 0
    for i in set1:
        if nums.count(i) > len(nums)//2:
            res = i
            break
    return res