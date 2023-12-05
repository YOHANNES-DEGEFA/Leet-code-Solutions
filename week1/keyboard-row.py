class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f_row = "qwertyuiopQWERTYUIOP"
        s_row = "asdfghjklASDFGHJKL"
        t_row = "zxcvbnmZXCVBNM"
        ans = []
        for word in words:
            fr_counter = 0
            sr_counter = 0
            tr_counter =0
            lenW = len(word)
            for char in word:
                if char in f_row:
                    fr_counter+=1
                elif char in s_row:
                    sr_counter +=1
                elif char in t_row:
                    tr_counter +=1
                else:
                    break
            if fr_counter == lenW or sr_counter == lenW or tr_counter == lenW:
                ans.append(word)
        return ans

