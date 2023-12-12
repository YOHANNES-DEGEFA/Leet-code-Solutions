class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0 

        def digitSum(num):
            sqrsSum = 0 
            while num != 0: 
                sqrsSum += (num%10)**2
                num //= 10

            return sqrsSum 


        while n != 1 and count < 10:
            n = digitSum(n)
            count += 1

        if n == 1: 
            return True 

        return False
        