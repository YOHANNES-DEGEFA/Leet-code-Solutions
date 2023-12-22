class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows, cols= len(matrix), len(matrix[0])
        ans = []

        for j in range(cols):
            temp = []
            
            for i in range(rows):
                temp.append(matrix[i][j])

            ans.append(temp)
        return ans