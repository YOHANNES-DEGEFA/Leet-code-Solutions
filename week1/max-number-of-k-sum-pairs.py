class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 0, N-1
        max_operations = 0 
        nums.sort()

        while l < r: 
            cur_sum =  nums[l] + nums[r]
            if cur_sum < k: 
                 l += 1 
            elif cur_sum > k: 
                r -= 1 
            else: 
                max_operations += 1 
                l += 1 
                r -= 1 
       
        return max_operations

            
            

        