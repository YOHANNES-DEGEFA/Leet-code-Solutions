class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set2 = set(nums2)
        for n in nums1: 
            if n in set2: 
                return n 

        return -1 
        