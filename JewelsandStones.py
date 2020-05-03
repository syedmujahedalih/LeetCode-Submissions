def numJewelsInStones(self, J: str, S: str) -> int:
    count = 0
    jewels = set(J)
    for i in S:
        if i in jewels:
            count+=1
    return count