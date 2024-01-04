class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r  = 0, len(nums)-1
        result = 0 

        while l< r:  
            if nums[l] + nums[r] < target: 
                # this assumes that if the sum of the element at position l and the one in at position r 
                # is less than target since the list is sorted we can for sure say that the sum of the element 
                # at the position l and those below between position l and and r is less than target 
                # meaning we can pairup element at pos l with other elements below and including the one at
                # position r hence  ans += r-l and we increment l since we are done with the current one. 
                result += r-l    
                l += 1 
            else: # if the sum is greater or equal to target just decrement r 
                r -= 1

        return result 

        



       
        