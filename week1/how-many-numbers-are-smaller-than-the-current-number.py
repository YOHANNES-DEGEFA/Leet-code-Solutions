class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []
        temp = sorted(nums)
        for i, n in enumerate(temp): 
            if n not in d: 
                d[n] = i
        
        for n in nums: 
            ans.append(d[n])

        return ans

        