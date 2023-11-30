class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
      return t*2 + num
    
    # Moral of the Problem: Patter recognation 
    # I didn't watch anyones solution I just observed the pattern by 
    # trying some test cases like n = 4 and t = 20 the answer was 44 then 
    # I came to the conclusion that the answer will always be 2*t + n 
        
        