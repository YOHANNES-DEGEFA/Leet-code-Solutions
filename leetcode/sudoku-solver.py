class Solution:
    def solveSudoku(self, board):
        empty, subBox, col, row = deque([]), defaultdict(set), defaultdict(set), defaultdict(set)
        # analyze the current status 
        for i in range(9):
            for j in range(9): 
                cur = board[i][j]
                if cur != '.': 
                    tmp = (i//3,j//3)
                     
                    subBox[tmp].add(cur)
                    col[j].add(cur)
                    row[i].add(cur)

                else: 
                    empty.append((i,j))

        
        def dfs(): 

            if not empty:   # if all the board is filled 
                return True 

            r, c = empty[0]
            tmp = (r//3, c//3)
            for n in '123456789': 
                if n not in row[r] and n not in col[c] and  n not in subBox[tmp]: 
                    row[r].add(n);   col[c].add(n);    subBox[tmp].add(n); empty.popleft()

                    board[r][c] = n

                    if dfs(): 
                        return True 
                    else: 
                        row[r].remove(n);   col[c].remove(n);   subBox[tmp].remove(n)
                        board[r][c] = '.'
                        empty.appendleft((r,c))
           
        dfs()
        # return board
       