class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows, cols = len(matrix), len(matrix[0])
        n = rows*cols
        answer = []
        visited = set()
        start = [0,0]
        r, c = 0, 0 
        for  i in range(len(matrix)):
           
            while c < cols:
                answer.append(matrix[r][c])
                c += 1 
           
            c -= 1   #because the last loop ended when c == cols 
            r += 1  #because we have already added the val at r, c 
            while r < rows:
                answer.append(matrix[r][c])
                r += 1 
                        
            # <-----
            c -= 1   # because we already have appended the value at r, c 
            r -= 1   # because the last loop ended when r == rows 
            while c >= i:
                        answer.append(matrix[r][c])
                        c -= 1 

            # @
            # |
            # |
            c += 1  # because the last loop ended when c == i-1
            r -= 1  # because we have already appended the value at r, c
            while r > i:
                        answer.append(matrix[r][c])
                        r -= 1 
            r += 1 # because r 
            c += 1 
            rows, cols = rows-1, cols-1
    

        return answer[:n]
        