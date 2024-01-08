class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        l, r = 0, 0 
        N, M = len(name), len(typed)
        
        while l < N:  
            count = 0 
            char = name[l]
            while l < N and name[l]  == char: 
                count += 1 
                l += 1
            
            count2 = 0 
            while r < M and typed[r] == char: 
                r += 1 
                count2 += 1 
            if count > count2: 
                return False
        
        if r != M: 
            return False
            
        return True 
        