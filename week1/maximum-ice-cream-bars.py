class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        coma = max(costs) +1 
        arr = [0]*coma 
        sorted_arr = []
        for cost in costs: 
            arr[cost] += 1 

        for i, freq in enumerate(arr):
            for j in range(freq):
                sorted_arr.append(i)

        i = 0 
        N = len(sorted_arr)
        result = 0 
        while i < N and coins - sorted_arr[i] >= 0: 
            coins -= sorted_arr[i]
            result += 1 
            i += 1 
        return result 



            
