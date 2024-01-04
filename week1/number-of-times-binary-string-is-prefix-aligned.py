class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right = res = 0
        for i, a in enumerate(flips, 1): # the number '1' inside the function tells enumerate to start indexing from one instead of the default 0.
            right = max(right, a)
            res += right == i
        return res
       