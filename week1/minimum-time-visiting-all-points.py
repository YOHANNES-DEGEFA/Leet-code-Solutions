class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minTime = 0 

        for i in range(len(points)-1):
            
            curX, curY = points[i]
            nextX, nextY = points[i+1]
            minTime += max(abs(nextX-curX), abs(nextY - curY))

        return minTime