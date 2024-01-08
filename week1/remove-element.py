class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l, r = 0, 0 
        coma, N = nums.count(val), len(nums)
        while r < N: 
            
            while l < r and  nums[l] != val: 
                l += 1
                
            while r < N and nums[r] == val: 
                r += 1 
            
            if r < N: 
                nums[l], nums[r] = nums[r], nums[l]
            
            l += 1 
            r += 1 
            
        return N - coma 
        