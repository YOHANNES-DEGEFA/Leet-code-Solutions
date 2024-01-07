class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','o','i','u'])
        
        l = cur_vowels = max_vowels = 0 
        
        for r in range(len(s)):
            
            if r - l + 1 > k: 
                if s[l] in vowels: 
                    cur_vowels -= 1 
                l += 1 
            
            if s[r] in vowels: 
                cur_vowels  += 1 
                
            if cur_vowels > max_vowels: 
                max_vowels = cur_vowels
                
        return max_vowels 
                
        
                
            
        