class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # simply find all the subarray that has less than or equal to k 
        # and find all the subarrays that has less than k odds numbers 
        # the answer would be the difference b/n the number of subarrays 
        # thath as <= k odd numbers and < k odd numbers

        def num_subarrays(nums,k): 

            answer = 0 
            l = 0 
            odds = 0 

            for r in range(len(nums)): 
                odds += nums[r] % 2
                while odds > k: 
                    odds -= nums[l]%2   # is 1 if the number is odd else 0
                    l += 1  
                answer += r-l+1 
            return answer 

        
        with_k, with_out_k = num_subarrays(nums,k) ,  num_subarrays(nums,k-1)

        return with_k - with_out_k
        