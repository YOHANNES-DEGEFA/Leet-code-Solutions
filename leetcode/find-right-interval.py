class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        ans = [-1]*N
        
        startPos = [x for x, y in intervals]
        startPos.sort()
        i = -1
        
        d = {x:i for i,(x,y) in enumerate(intervals)}
        
        for start, end in intervals:
            idx = bisect_left(startPos,end)
            i  += 1
            
            if idx >= N: 
                continue 
            ans[i] = d[startPos[idx]]
        return ans 
            