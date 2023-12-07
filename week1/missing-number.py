class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        wosagn = len(nums)
        expected = (wosagn*(wosagn + 1))/2
        return int(expected - sum(nums))