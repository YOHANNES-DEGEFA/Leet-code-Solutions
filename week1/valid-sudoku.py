class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # colsMap = {d:[] for d in range(9)}
        # rowsMap  = {d:[] for d in range(9)}
        # sub_gridsMap = {d:[] for d in range(9)}

        #collect elements in each row
        for i in range(9):
            cur_row = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in cur_row: 
                        return False
                    cur_row.add(board[i][j])

        #collect elements in each column
        for j in range(9):
            cur_col = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in cur_col: 
                        return False
                    cur_col.add(board[i][j])

        # if any(len(s) != len(set(s)) for s in colsMap.values()):
        #     return False

        
        # if any(len(s) != len(set(s)) for s in rowsMap.values()):
        #     return False

        
        for k in range(9):
            for i, j in [(1,1),(1,4),(1,7), (4,1),(4,4), (4,7),(7,1),(7,4),(7,7)]:
                temp = set()
                for c  in range(i-1,i+2):
                    for d in range(j-1,j+2):
                        if board[c][d] != '.':
                            if  board[c][d] in temp: 
                                return False
                            temp.add( board[c][d])
        return True 



        

        

        
        