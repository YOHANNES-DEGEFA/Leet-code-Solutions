from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        d = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])


        arr = sorted(d.keys())
        ans = []
        flag = 1 
        for k in arr: 
            if flag:
                temp = d[k][::-1]
            
                for n in temp: 
                    ans.append(n)
                flag = 0  
           
            else: 
                temp = d[k]
                for n in temp:
                    ans.append(n)
                flag = 1 
    
        return ans


