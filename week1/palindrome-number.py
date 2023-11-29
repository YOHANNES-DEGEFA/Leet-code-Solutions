class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        first = []
        if x < 0: return 0
        while x > 0: 
            first.append(x%10)
            x //= 10
        return first[::-1] == first
        