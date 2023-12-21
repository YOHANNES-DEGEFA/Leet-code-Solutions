class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)): digits[i] = str(digits[i])
        num_plus_one  = eval(''.join(digits)) + 1 
        arr = [int(x) for x in str(num_plus_one)]

        return arr
        