class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Find maximum average obtained from any subarray of length k 
            Args: 
                nums = array of the given numbers 
                k = length of the subarray to be averaged 
            Returns: 
                The maximum average achieved
        """
        max_avg = float('-inf')
        cur_sum = 0 
        l = 0 
        
        for r in range(len(nums)):
            
            if r-l+1 > k: 
                cur_sum -= nums[l]
                l += 1 
                
            cur_sum += nums[r]
            if r-l+1 == k: 
                cur_avg = cur_sum/k

                if cur_avg > max_avg: 
                    max_avg = cur_avg
                    
        return max_avg 


            