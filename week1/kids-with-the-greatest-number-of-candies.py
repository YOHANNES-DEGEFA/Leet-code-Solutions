class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxElem = max(candies)
        answer = []

        for n  in candies: 
            answer.append(n+extraCandies >= maxElem)

        return answer
        