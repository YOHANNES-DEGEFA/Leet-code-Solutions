class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0 
        piles.sort()

        n = len(piles)//3 

        result = 0 
        # one important decision is to not include the smallest n elements to our result
        for i in range(n,len(piles), 2):
            result += piles[i]

        return result