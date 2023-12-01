class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []
        for i in range(min(len(word1),len(word2))):
            arr.append(word1[i])
            arr.append(word2[i])
        arr.extend(word1[i+1:])
        arr.extend(word2[i+1:])
        return ''.join(arr)
        