class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        d = Counter()
        m, n = len(s1), len(s2)
        
        if m > n: 
            return False 
   
        l = 0 
      
        for r in range(n): 
            
            d[s2[r]] += 1 
            while  r-l+1 >= m: 
                if r-l+1 == m and freq == d: 
                    return True
                d[s2[l]] -= 1 
                l += 1 
            
        return False
        