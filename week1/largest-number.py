
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        """
        Finds the largest number that can be formed by concatenating non-negative integers.

        Args:
            nums: A list of non-negative integers.

        Returns:
            The largest number that can be formed by concatenating the integers in nums.
        """
        if all(x==0 for x in nums): 
            return  "0"
        nums = list(map(str,nums))
        
        def custom_comparator(num1, num2): 
            return num1 + num2 > num2 + num1
        
        for i in range(len(nums)-1): 
            for j in range(len(nums)-i-1): 
                if not custom_comparator(nums[j],nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        return ''.join(nums)
        