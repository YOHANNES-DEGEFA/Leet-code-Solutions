class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCount = {}

        for match in matches: 
            p1, p2 = match 
            if p2 in loseCount:
                loseCount[p2] += 1 

            else:
                loseCount[p2] = 1

            if p1 not in loseCount:
                loseCount[p1] = 0 

        list0, list1 = [], []

        for k, v  in loseCount.items():
            if v == 0:
                list0.append(k)
            elif v == 1: 
                list1.append(k)

        list0.sort()
        list1.sort()

        return [list0, list1]