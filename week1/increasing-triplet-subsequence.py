class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        preffix = [0] * N
        suffix = [0]*N 

        preffix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1,N):
            preffix[i] = min(preffix[i-1], nums[i])

        for j in range(N-2,-1,-1):
            suffix[j] = max(suffix[j+1], nums[j])

        
        for i, num in enumerate(nums):
            if preffix[i] < num < suffix[i]:
                return True 

        return False

                
        