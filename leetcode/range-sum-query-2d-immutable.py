class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        
        prefix_sum = [[0]*(col + 1)  for _ in range(row+1)]
        prefix_sum[0][0] = matrix[0][0]
        
        
        for i in range(row): 
            for j in range(col):
                prefix_sum[i+1][j+1] += matrix[i][j] +  prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j]
                
        self.prefix_sum = prefix_sum 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        
        answer = self.prefix_sum[row2+1][col2+1] + self.prefix_sum[row1][col1]  - self.prefix_sum[row2+1][col1]  - self.prefix_sum[row1][col2+1] 
       
        return answer 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)