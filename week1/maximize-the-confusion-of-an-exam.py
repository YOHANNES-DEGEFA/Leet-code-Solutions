class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq = {"T":0,"F":0}
        
        l = 0 
        answer = 1
        for r in range(len(answerKey)):
            freq[answerKey[r]] += 1 
            cur_freq = freq["T"] if freq["T"] > freq["F"] else freq["F"] 
            
            while (r-l+1) - cur_freq > k: 
                freq[answerKey[l]] -= 1 
                l += 1 
            if r-l+1 > answer: 
                answer = r-l+1 
        
        return answer