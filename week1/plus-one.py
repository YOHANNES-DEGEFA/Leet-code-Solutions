class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: 
            digits[-1] += 1 
            return digits 

        carry = 1 
        for i in range(len(digits)-1, -1, -1):
            d = carry + digits[i]
            carry = d//10 
            digits[i]  = d%10

        if carry: 
            digits.insert(0,carry)

        return digits 