class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives, positives, answer = [], [], []
        for num in nums: 
            if num > 0: 
                positives.append(num)
            else: 
                negatives.append(num)
        positives = positives[::-1]
        negatives = negatives[::-1]
        for _ in range(len(positives)):
            answer.append(positives.pop())
            answer.append(negatives.pop())
        return answer

