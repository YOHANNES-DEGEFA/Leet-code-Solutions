class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur_sum = max_sum = l = 0 
        seen = set()

        for r in range(len(nums)): 
            
            while nums[r] in seen: 
                seen.remove(nums[l])
                cur_sum -= nums[l]
                l += 1 
            seen.add(nums[r])
            cur_sum += nums[r]
            
            if cur_sum > max_sum: 
                max_sum = cur_sum 

        return max_sum
        