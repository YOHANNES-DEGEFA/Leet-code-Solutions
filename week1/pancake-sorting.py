class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(arr), 1, -1 ):
            idx = arr.index(i) 
            k = idx + 1
            arr = arr[:k][::-1] + arr[k:]
            arr = arr[:i][::-1] + arr[i:]
      
            ans.append(k)
            ans.append(i)


            if arr == sorted(arr):
                return ans 

        return ans 








        # n = len(arr)
        # ans  = []
        # for i in range(n,1,-1):
        #     idx = arr.index(i)
        #     arr[:idx+1] = arr[:idx+1][::-1]
        #     arr[:i] = reversed(arr[:i])
        #     ans.append(idx)
        #     if arr == sorted(arr):
        #         return ans
            
        #     print(arr, idx)
        # print(arr)
        # return ans



            
        
    