class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
     
        zeros = l = answer = 0 
        
        for r in range(len(nums)):
            
            zeros += nums[r]==0 
            while zeros > 1: 
                zeros -= nums[l] == 0
                l += 1 
            
            if r-l > answer: 
                answer = r-l
                
        return answer
                
            
        