class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
       
        def feasible(divisor): 
            totSum = 0 
            for num in nums: 
               
                totSum = totSum + (num-1)//divisor+1
                    
            return totSum 
        
        
        low = 1
        high = max(nums)
        while high >= low: 
            
            mid = (high + low)//2 
            
            if feasible(mid) > threshold: 
                low = mid+1 
            else:
                high = mid - 1 

        return low