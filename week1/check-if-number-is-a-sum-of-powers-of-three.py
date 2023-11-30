class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr = []
        while n != 0:
            arr.append(n%3)
            n //= 3 
        if 2 in arr:
            return False
        return True
    
        

        

       
