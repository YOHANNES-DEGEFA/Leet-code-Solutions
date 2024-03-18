class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
       
        def searchRow(start, end, mid): 

            while start <= end: 
                row = (start+end)//2 

                if matrix[row][mid] > target: 
                    end = row-1
                elif matrix[row][mid] < target: 
                    start = row + 1 
                else: 
                    return 0, True 

            return start, False 

            
        def binarySearch(arr): 
            high, low = len(arr)-1, 0 

            while low <= high: 

                mid = (low+high)//2

                if arr[mid] > target: 
                    high = mid-1 

                elif arr[mid] < target: 
                    low = mid + 1
                else: 
                    return mid 
            return -1
        row, col = len(matrix), len(matrix[0])

        r, x = searchRow(0, row-1, col//2)
      
        if x: 
            return True 
        print(r)
        if r >= row: r -= 1
        if binarySearch(matrix[r]) != -1 : 
            return True 
        elif r > 0 and binarySearch(matrix[r-1]) != -1: 
            return True
        elif r < row -1 and binarySearch(matrix[r+1]) != -1: 
            return True

        return False