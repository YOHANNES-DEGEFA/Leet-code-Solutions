import  math
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        oneFourth = len(arr)//4 

        for i in range(len(arr)-oneFourth):
            if arr[i] == arr[i+oneFourth]:
                return arr[i]
        return arr[-1]
        