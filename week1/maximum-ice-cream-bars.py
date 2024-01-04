class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0;  costs.sort();  i, N = 0, len(costs)
        while i < N and coins - costs[i] >= 0: 
            ans += 1 
            coins -= costs[i]
            i += 1 
        return ans 
