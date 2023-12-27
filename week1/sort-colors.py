class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3

        for num in nums: 
            freq[num] += 1 

        w, r, b = 1 , 0, -1
        idx = 0 
        for i in range(3):
            if i == 0: 
                for i in range(freq[i]):
                    nums[idx] = 0 
                    idx += 1 
            elif i == 1:
                for i in range(freq[i]):
                    nums[idx] = 1
                    idx += 1 

            else:
                for i in range(freq[i]):
                    nums[idx] = 2
                    idx += 1 




            
        