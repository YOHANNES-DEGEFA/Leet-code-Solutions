class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        answer = len(nums) +1 
    
        l, cur_sum, N= 0,0, len(nums)
        for r in range(N): 
            cur_sum += nums[r]
            while r < N and cur_sum >= target: 
                answer = min(answer, r-l+1)
                cur_sum -= nums[l]
                l += 1 

        return answer if answer < N +1 else 0
        