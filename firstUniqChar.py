from collections import Counter

def firstUniqChar(s: str):
    c1 = Counter(s)
    result = 0
    if s=="":
        return -1
    for i in s:
        if c1[i]==1:
            result = s.index(i)
            break
    else:
        result = -1
    return result