class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_glass_sum = 0 

        for i in range(1, len(grid)-1):
            for j in range(1,len(grid[0])-1):
                cur_sum = 0
                up = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                down = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                cur_sum += up + grid[i][j] + down

                if max_glass_sum < cur_sum: 
                    max_glass_sum = cur_sum 

        return max_glass_sum 
        