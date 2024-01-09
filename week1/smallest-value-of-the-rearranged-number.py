class Solution:
    def smallestNumber(self, num: int) -> int:
        """Rearranges digits of num iteratively to minimize its value, preserving the sign."""
        sign = 1 
        if num == 0: 
            return 0 
        
        num = str(num)
        if int(num) < 0: 
            num = num[1:]
            sign = -1 
        digits = []
        for digit in num: 
            digits.append(digit)
        
        digits.sort()
        i = 0 
        while digits[i] == '0': 
            i += 1 
            
        digits[0], digits[i] = digits[i], digits[0]
            
            
        if sign == 1: 
            return int(''.join(digits))
        else: 
            digits.sort(reverse=True)

        
        return -1*int(''.join(digits))
            
        
            
        