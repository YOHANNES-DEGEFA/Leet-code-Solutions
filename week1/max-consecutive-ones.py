class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max, global_max = 0, 0

        for n in nums:
            if n: 
                cur_max += 1 
            else: 
                cur_max = 0

            if cur_max > global_max:
                global_max = cur_max

        return global_max