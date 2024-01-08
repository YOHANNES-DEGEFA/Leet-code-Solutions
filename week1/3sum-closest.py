class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        t, ans, N, diff = target, 0 , len(nums), float("inf")
      
        for i in range(N):
            n = nums[i]
            l, r = i +1, N-1
            while l < r: 
                tm = n + nums[r] + nums[l]
                if tm >  t:
                    cm = abs(t-tm)
                    if cm < diff:
                        ans = tm
                        diff = cm 
                    r-=1 
                elif  tm < t:
                    cm = abs(t-tm)
                    if cm < diff:
                        ans = tm
                        diff = cm 
                    l += 1 
                else: 
                    return  tm 

        return ans