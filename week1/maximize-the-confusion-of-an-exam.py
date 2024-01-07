class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq = [0,0]
        
        l = cur_max =  0 
        answer = 1
        for r in range(len(answerKey)):
            cur_idx = 1 if answerKey[r] == "T" else 0 
            freq[cur_idx] += 1 
            
            if freq[cur_idx] > cur_max: 
                cur_max = freq[cur_idx] 
            
            while (r-l+1) - cur_max > k:
                cur_idx = 1 if answerKey[l] == "T" else 0 
                freq[cur_idx] -= 1 
                l += 1 
            if r-l+1 > answer: 
                answer = r-l+1 
        return answer