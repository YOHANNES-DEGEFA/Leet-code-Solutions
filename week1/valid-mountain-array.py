class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i, j = 1, N - 1

        if len(arr) < 3: 
            return False 

        while i < N and arr[i] > arr[i-1]:
            i += 1 

        while j > 0 and  arr[j] < arr[j-1]:
            j -= 1 

        i -= 1 

        if i == N-1 or i == 0:
            return False
        
        return i == j 