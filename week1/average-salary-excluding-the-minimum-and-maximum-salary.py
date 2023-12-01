class Solution:
    def average(self, salary: List[int]) -> float:
        maxElement, minElement = float("-inf"), float('inf')

        for num in salary:
            if num < minElement: 
                minElement = num

            if num > maxElement: 
                maxElement = num 

        totalSum = 0 
        for n in salary: 
            totalSum += n 

        totalSum -= (minElement+maxElement)
        answer = totalSum/(len(salary)-2)
        return answer 

        