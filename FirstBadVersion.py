#isBadVersion API is already defined in LeetCode environment

def firstBadVersion(self, n):
    start = 1
    end = n 
    while start < end:
        mid = (start + end)//2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid+1
    return start
                                 