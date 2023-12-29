class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = 0 
        cur_diff = 0
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                cur_diff += 1 
            res +=  cur_diff

        return res
       


        