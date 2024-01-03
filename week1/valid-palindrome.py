class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1
      
        while l < r: 
            if s[l].isalnum() and s[r].isalnum():
                if s[l] != s[r]:
                    return False
                l +=1 
                r -= 1
            elif s[r].isalnum():
                l += 1
            elif s[l].isalnum():
                r -= 1 
            else: 
                l +=1 
                r -= 1
        return True

        