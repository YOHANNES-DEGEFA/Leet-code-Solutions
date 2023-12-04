class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()

        words = words[::-1]
        ansLen = len(max(words, key=len))

        answer = []
        for i in range(ansLen):
            s = ''
            for j in range(len(words)):
                if i < len(words[j]):
                    s = words[j][i] + s
                elif s: 
                    s = ' ' + s
            answer.append(s)
        return answer 
        