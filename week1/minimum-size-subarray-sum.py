class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = float("inf")
        
        l = cur_sum = 0 
        for r in range(len(nums)):
            
            cur_sum += nums[r]
            
            while cur_sum >= target: 
                cur_sum -= nums[l]
                answer = min(answer, r-l+1)
                l += 1 
                
            
            
        return answer if answer < float('inf') else 0 
        