class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum = [0]*(len(self.nums)+1)
        # # print(self.nums, prefix_sum)
        # for i in range(len(self.nums)):
        #     prefix_sum[i] = prefix_sum[i-1] + self.nums[i]
        
        # print(self.nums, prefix_sum)
        return sum(self.nums[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)