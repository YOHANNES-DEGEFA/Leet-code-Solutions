class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: 
            return nums
        l, r = 0, 1 
        while True:
            while r < len(nums) and nums[r] == 0: 
                r += 1 
            while l < r and nums[l] != 0: 
                l += 1
            
            if r >= len(nums):
                break
                
            if nums[r] and not nums[l]:
                nums[r], nums[l] = nums[l], nums[r]
            
            r += 1 

            
        