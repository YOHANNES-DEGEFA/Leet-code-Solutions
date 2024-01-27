class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        alphabet_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 
                             'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 
                                  11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
                                      18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
       
        s_len = len(s)

        suffix_sum = [0]*(s_len+1)
        for i in range(s_len-1,-1,-1): 
            suffix_sum[i] += shifts[i] + suffix_sum[i+1]

        answer = []
       
        for i in range(s_len): 
            key = (ord(s[i]) + suffix_sum[i] - 97)%26
            answer.append(alphabet_dict[key])

        return ''.join(answer)
        