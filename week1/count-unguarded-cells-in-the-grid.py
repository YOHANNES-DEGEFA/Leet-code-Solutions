class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        row, col = m, n
        ans = 0 
        
        grid = [[0]*col for _ in range(row)]


        def guard_sees(i,j):
            
            up = i-1 
            #expand to North 
            while up > -1 and temp[up][j] == 0:
                print(grid[up][j] == 0)
                grid[up][j] = 1 
                up -= 1 

            left = j-1
            # expand to West 
            while left > -1 and temp[i][left] == 0:
                grid[i][left] = 1 
                left -= 1 

            down = i +1 
            # expand to South 
            while down < row and temp[down][j] == 0: 
                grid[down][j] = 1 
                down += 1 

            right = j+1 
            #expand to East
            while right < col and temp[i][right] == 0: 
                grid[i][right] = 1 
                right += 1 

        for pos in guards: 
            r, c = pos
            grid[r][c] = 1 

        for p in walls: 
            rr, cc = p
            grid[rr][cc] = 2 

        temp = deepcopy(grid)

        for cur_pos in guards: 
            i, j = cur_pos
            guard_sees(i,j)
        
        print(grid)
        for i in range(row): 
            for j in range(col):
                if grid[i][j] == 0: 
                    ans += 1 

        return ans 


        



        
        