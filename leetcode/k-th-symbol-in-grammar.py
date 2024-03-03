class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0 
        n -= 1 
        l , r = 0, 2**n
        while n:

            mid = (l+r)//2
            if mid >= k: 
                r = mid
            else: 
                l = mid + 1
                ans = 0 if ans==1 else 1
            n-=1

        return ans


        
        
