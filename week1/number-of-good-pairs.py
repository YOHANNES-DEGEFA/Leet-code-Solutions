class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # both time 84.86% and space 92.33% effiecent  but, not a stable 
        goodPairs = 0
        for i in range(len(nums)):
            k = nums[i]
            for j in range(i+1,len(nums)):
                if k == nums[j]:
                    goodPairs +=1
                
        return goodPairs
                
"""
#Time effiecent 99.32% , Space ineffiecent 31.89% 
lenNum = len(nums)
goodPairs = 0
for i in range(lenNum):
    for j in range(i+1,lenNum):
        if nums[i] == nums[j]:
            goodPairs +=1

return goodPairs
"""