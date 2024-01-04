class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        """Returns a list of indices with the highest division score in the binary array nums."""

        n = len(nums)
        left_zeros = 0
        right_ones = sum(nums)  # Count the total number of 1s initially
        mx = right_ones  # Initialize mx with the maximum possible score at index 0
        ans = []

        for i in range(n + 1):  # Iterate from 0 to n (inclusive)
            score = left_zeros + right_ones
            if score == mx:
                ans.append(i)
            elif score > mx:
                mx = score
                ans = [i]

            if i < n:  # Update counts for the next iteration
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1

        return ans

        # N = len(nums)
        # d = {}
        # prefix = [0]*(N+1)
        # suffix = [0]*(N+1)

        # prefix[1] = int(nums[0] == 0)
        # suffix[-2] = int(nums[-1] == 1)
     
        # for i in range(1,len(nums)):
        #     prefix[i+1] = prefix[i] + int(nums[i]==0)
          

        # for i in range(len(nums)-1, -1, -1):
        #     suffix[i] = suffix[i+1] + int(nums[i] == 1)
        #     print(suffix)
            
        # for i in range(1,N+1):
        #     d[i-1] = prefix[i-1] + suffix[i]

        # print(prefix, suffix)
        # coma = max(d.values())

        # ans = []
        # for k, v in d.items():
        #     if v == coma: 
        #         ans.append(k)

        # return ans 

        
        