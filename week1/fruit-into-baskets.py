class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLen = 1
        l  = 0 
        seen = defaultdict(int)

        for r in range(len(fruits)): 
            seen[fruits[r]] += 1 
            while len(seen) > 2: 
                seen[fruits[l]] -= 1 
                if seen[fruits[l]] == 0: 
                    del seen[fruits[l]]
                l += 1 
            windowLen = r-l+1
            if windowLen > maxLen: 
                maxLen = windowLen
        return maxLen

        