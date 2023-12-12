class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evensSum = sum(x for x in nums if x%2 == 0)

        answer = []
        for query in queries: 
            val, i = query
            
            if (nums[i] %2 == 0 and val % 2 == 1):
                evensSum -= nums[i]
            elif (nums[i]%2 == 0 and val % 2 == 0):
                evensSum += val
            elif (nums[i]%2 == 1 and val % 2 == 1):
                evensSum += nums[i] + val
            
            nums[i] += val

            answer.append(evensSum)
    
        return answer
        