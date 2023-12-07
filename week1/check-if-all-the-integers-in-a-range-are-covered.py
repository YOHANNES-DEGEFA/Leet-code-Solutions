class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        rangeSet = set(x for x in range(left,right+1))
        for s, e in ranges:
            for i in range(s,e+1):
                if not rangeSet:
                    return True
                if i in rangeSet:
                    rangeSet.remove(i)
        if not rangeSet:
            return True
        return False
        