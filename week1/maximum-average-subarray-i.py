class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0 
        cur_sum = 0
        ans = float('-inf')
        for r in range(len(nums)):

            if r-l+1 > k: 
                cur_sum -= nums[l]
                l += 1 
            cur_sum += nums[r]

            if r-l+1 == k: 
                ans = max(ans, cur_sum/(k))

        return ans 
        