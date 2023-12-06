class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        i, j = 0, 1 

        for num in nums:
            if num > 0: 
                answer[i] = num 
                i += 2

            else: 
                answer[j] = num 
                j += 2

        return answer 
                