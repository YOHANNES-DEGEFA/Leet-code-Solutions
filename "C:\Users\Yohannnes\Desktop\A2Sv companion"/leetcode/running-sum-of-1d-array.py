class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # just return the prefix sum of the array 
        for i in range(1,len(nums)): 
            nums[i] += nums[i-1]
            
        return nums
