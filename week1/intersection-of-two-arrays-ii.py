class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 , freq2 = defaultdict(int), defaultdict(int)
        set1, set2 = nums1, nums2 
        res = []

        for num in nums1:
            if num in set2: 
                freq1[num] += 1 

        for num in nums2:
            if num in set1: 
                freq2[num] += 1

        for num in freq1: 
            for i in range(min(freq1[num], freq2[num])):
                res.append(num)

        return res

         
        