class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, freq, ans = 0, defaultdict(int), 0 
        max_freq = 0 
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq,freq[s[r]])
            while (r-l+1) - max_freq > k :
                freq[s[l]] -= 1
                l += 1 
            ans = max(ans, r-l+1)   
        return ans 







        # freq = defaultdict(int)
        # l = res =  0
        # maxF = 0
        # for r, c in enumerate(s):
        #     freq[c] += 1
        #     # using maxF works because at the end of the day we need to find the the window in which
        #     # the difference between the window length and maxF is minimum, meaning we can replace
        #     # as much charachters as allowed (i.e k ) in this window while mai
        #     maxF = max(maxF,freq[c])
        #     while r-l+1 - maxF > k: 
        #         freq[s[l]] -= 1
        #         l += 1 
        #     res = max(res,r-l+1)

        # return res
                
        




        #Buggy 

        # ans = 0
        # freq = [0]*26

        # l, r = 0, 0 

        # while r < len(s):

        #     while (r-l+1)-max(freq) > k:
        #         freq[ord(s[l])-65] -= 1 
        #         l += 1
        #     ans = max(ans,r-l+1)
        #     r += 1
        # return ans 



        # ans = 0
        # freq = [0]*26

        # l, r = 0, 0 

        # while r < len(s):

        #     while (r-l+1)-max(freq) > k:
        #         freq[ord(s[l])-65] -= 1 
        #         l += 1
        #     ans = max(ans,r-l+1)
        #     r += 1
        # return ans 