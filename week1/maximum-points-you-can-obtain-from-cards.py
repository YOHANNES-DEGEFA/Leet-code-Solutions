class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        N, min_sum, cur_sum = len(nums), float('inf'), 0 
        tot_sum = sum(nums)
        coma = N - k 
       

        l = 0 
        for r in range(N): 
            cur_sum += nums[r]
            while r-l+1 > coma: 
                cur_sum -= nums[l]
                l += 1

            if r-l+1 == coma: 
                min_sum = min(min_sum,cur_sum)

        return tot_sum - min_sum