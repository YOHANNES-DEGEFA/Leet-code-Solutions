class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = len(nums)//3
        d = {}
        ans = set()

        for i in nums:
            d[i] = 1 + d.get(i,0)
            if d[i] > check:
                ans.add(i)
        res =  []
        for j in ans:
            res.append(j)
        return res