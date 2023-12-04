class Solution:
    def largestGoodInteger(self, num: str) -> str:
        lst = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                lst.append(num[i])

        if not lst:
            return ''

        return max(lst)*3
        