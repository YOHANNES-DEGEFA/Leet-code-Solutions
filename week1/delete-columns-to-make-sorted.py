class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        rows, cols = len(strs), len(strs[0])
        answer = 0

        for j in range(cols):
            prev = strs[0][j]
            for i in range(1, rows):
                if prev > strs[i][j]:
                    answer += 1 
                    break
                prev = strs[i][j]

        return answer

        