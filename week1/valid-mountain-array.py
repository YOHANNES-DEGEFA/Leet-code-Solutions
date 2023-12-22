class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
       
       if len(arr) < 3: return False
      #Just return false if you get an adjacent duplicates
       for i in range(1,len(arr)):
            if arr[i-1] == arr[i]:
                return False
       idx = -1
       count = 0 
       for i in range(1,len(arr)-1):
           if  arr[i-1] < arr[i] > arr[i+1]:
               idx = i 
               count += 1

       if count == 1: 
           first_point = arr[:idx] == sorted(arr[:idx])
           second_point = arr[idx+1:] == sorted(arr[idx+1:], reverse=True)
           if first_point and second_point: 
               return True
           else: 
               return False
       else:
            return False