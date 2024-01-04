class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1

        if len(nums) == 1: 
            return 1

        l, r, N = 0, 1, len(nums)
        while r < N: 
            if nums[l] == nums[r]:
                nums[r] = 101
            else: 
                ans += 1 
                l = r 

            r += 1 

        l, r = 0, 1 
        while True: 
            while r < N and nums[r] == 101: 
                r += 1 

            while l < r and nums[l] != 101: 
                l += 1 

            if r >= N : 
                break 
            if nums[l] == 101: 
                nums[l], nums[r] = nums[r], nums[l]
            
            r += 1 
        return ans 
        