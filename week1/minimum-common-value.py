class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        N, N2 = len(nums1), len(nums2)
        i = i2 = 0 
        while i < N and i2 < N2: 
            if nums1[i] > nums2[i2]: 
                i2 += 1 

            elif nums1[i] < nums2[i2]:
                i += 1 

            else: # if they both are equal we have found our answer, so return it
                return nums1[i] 

        return -1


        