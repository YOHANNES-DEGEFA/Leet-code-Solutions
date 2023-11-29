class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minString= min(strs,key = len)

        answer = ''

        for j in range(len(minString)):
            if all(strs[i][j]==minString[j] for i in range(len(strs))):
                answer += minString[j]
            else: 
                break
        return answer  
        