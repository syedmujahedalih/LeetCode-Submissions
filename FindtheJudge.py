def findJudge(N: int, trust: List[List[int]]):
                if N==1:
                        return 1
                people = defaultdict(set)
                k = set()
                for p,j in trust:
                        people[j].add(p)
                        k.add(p)
                for i in people:
                        if len(people[i])==N-1 and i not in k:
                                return i
                return -1
