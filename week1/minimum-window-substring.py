class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def checker(count, target): 
            if len(count) != len(target): 
                return False 
            
            for k in target: 
                if k not in count: 
                    return False 
                if target[k] > count[k]: 
                    return False 

            return True
            
        N = len(s)
        minSub, minLen = '' , N + 1 

        target = Counter(t)
        count = Counter()
        l = 0 
        for r in range(N): 
            if s[r] in target: 
                count[s[r]] += 1 
            
            while checker(count,target): 
                if r-l+1 < minLen: 
                    minLen = r-l+1 
                    minSub = s[l:r+1]
                if s[l] in count: 
                    count[s[l]] -= 1 
                l += 1 

        return minSub 

        