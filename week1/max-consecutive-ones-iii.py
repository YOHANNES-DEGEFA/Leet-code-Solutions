class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0 
        
        l = 0 
        answer = 0 
        for r in range(len(nums)): 
            zeros += nums[r] == 0 
            
            while zeros > k: 
                if nums[l] == 0: 
                    zeros -= 1 
                l += 1
            if r-l+1 > answer: 
                answer = r-l+1 
                
        return answer 
        