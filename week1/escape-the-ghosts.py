class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        x1, y1 = target[0], target[1]
        minTime = abs(x1) + abs(y1)

        def findMinTime(x2,y2):
           return abs(x2-x1) + abs(y2- y1)

        
        for ghost in ghosts: 
            curMin = findMinTime(ghost[0],ghost[1]) 
            if curMin <= minTime:
                return False


        return True