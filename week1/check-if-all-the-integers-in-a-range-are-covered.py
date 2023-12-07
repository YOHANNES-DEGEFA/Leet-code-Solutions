class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        numSet = {x for x in range(left,right+1)}

        for r in ranges: 
            start, end = r
            for num in range(start, end+1):
                if num in numSet: 
                    numSet.remove(num)

                if not numSet: 
                    return True

        return False
        