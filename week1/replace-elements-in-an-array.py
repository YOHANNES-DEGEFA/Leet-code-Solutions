class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            d[n] = i 

        for operation in operations: 
            n, cur = operation
            nums[d[n]] = cur
            d[cur] = d[n]
            del d[n]

        return nums