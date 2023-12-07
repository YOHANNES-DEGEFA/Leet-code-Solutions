class Solution:
    def largestOddNumber(self, num: str) -> str:
        k = len(num) -1
        while k>-1:
            if int(num[k])%2 != 0:
                return num[:k+1]
            k-=1
        return ''
