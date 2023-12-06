class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ans = []
        nums1 = nums[:n]
        nums2 = nums[n:]
        j = 0
        for i in nums1:
            ans.append(i)
            while j < len(nums2):
                ans.append(nums2[j])
                j+=1
                break

        return ans