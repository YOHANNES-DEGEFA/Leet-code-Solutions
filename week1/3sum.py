class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n = len(nums)-1
        ans = []
        seen = set()

        for i in range(n): 
            l , r  = i + 1, n 

            while l < r:
                temp =  nums[l] + nums[r] + nums[i]
                if temp > 0: 
                    r -= 1 
                elif temp < 0: 
                    l += 1 
                else:
                    temp = (nums[i], nums[l],nums[r])
                    if temp not in seen: 
                        ans.append(temp)
                    seen.add(temp)
                    r -= 1 
                    l += 1 

        return ans 


            