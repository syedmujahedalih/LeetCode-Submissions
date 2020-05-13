"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

"""

class Solution:
        def removeKdigits(self, num: str, k: int) -> str:
                stack=[]
                delnums = k
                for item in num:
                        while delnums and stack and stack[-1] > item:
                                stack.pop()
                                delnums-=1
                        stack.append(item)
                result="".join(stack[0:len(num)-k]).lstrip("0")
                if len(result):
                        return result
                else:
                        return "0"
        