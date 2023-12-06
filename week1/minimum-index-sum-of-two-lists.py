class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {string:i for i, string in enumerate(list1)}
        d2 = {string:i for i, string in enumerate(list2)}
        d3 = {}

        answer = []
        minIdxSum = float("inf")
        for string in list1: 
            if string in d2: 
                curSum = d[string] + d2[string]
                if curSum <= minIdxSum:
                    minIdxSum = curSum 
                    d3[string] = curSum

        leastIdxSum = min(d3.values())

        for k, v in d3.items(): 
            if v == leastIdxSum: 
                answer.append(k)
        return answer

        