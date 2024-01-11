class Solution:
    def balancedString(self, s: str) -> int:


        def checker(d,d2): 
            if len(d) != len(d2): 
                return False 
            
            for k in d: 
                if k not in d2: 
                    return False 
                if d[k] > d2[k]: 
                    return False 

            return True 

        N = len(s)
        need = N//4
        minLen  = float('inf')
    
        count = Counter(s)
        d = defaultdict(int)
        is_balanced = True
        for char in count:
            val = count[char]
            if val > need: 
                is_balanced = False
                d[char] = val - need 

        d2 = defaultdict(int)
        
        if is_balanced: 
            return 0
        l = 0 
    
        for r in range(N): 
            if s[r] in d:
                d2[s[r]] += 1 

            while checker(d,d2): 
                # print(d2,d,l,r)
                minLen = min(minLen, r-l+1)
                if s[l] in d: 
                    d2[s[l]] -= 1 
                l += 1

        return minLen 

        