class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxWidth = 0 
        points.sort()

        for i in range(1,len(points)):
            maxWidth = max(maxWidth, points[i][0]-points[i-1][0])

        return maxWidth
        