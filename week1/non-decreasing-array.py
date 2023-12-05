class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0 
        idx = 0 
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                idx = i-1
                count += 1 
            if count > 1: 
                return False
        
        if idx == 0 or idx >= len(nums)-2:
            return True

        if nums[idx-1] <= nums[idx+1] or nums[idx] <= nums[idx+2]:
            return True

        return False
        

      
        