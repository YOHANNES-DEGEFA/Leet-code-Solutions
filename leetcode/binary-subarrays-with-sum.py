class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def subarray_count(nums,goal):
            answer = l = cur_sum = 0 

            for r in range(len(nums)): 
                cur_sum += nums[r]
                while l <= r and cur_sum > goal: 
                    cur_sum -= nums[l]
                    l += 1
                answer += r-l+1 
            return answer 

        return subarray_count(nums,goal) - subarray_count(nums,goal-1)