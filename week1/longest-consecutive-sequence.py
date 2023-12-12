class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        numsSet = set(nums)
        answer = 0
        for num in nums: 
            
            if num -1 not in numsSet: 

                count = 0  
                while num in numsSet: 
                    num += 1
                    count += 1 

                if count > answer:
                     answer = count

        return answer

