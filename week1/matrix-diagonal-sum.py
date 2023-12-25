class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        i = 0 
        j = n-1
        l = 0 
        while i < n: 
            ans += mat[i][i]
            i += 1 

        while j > -1 and l < n: 
            ans += mat[l][j]
            j -= 1 
            l += 1 

        k = n//2
        # if the matrix intersects substract the value at the intersection since it has added 2 times 
        if n %2 == 1:
            ans -= mat[k][k]

        return ans 


        