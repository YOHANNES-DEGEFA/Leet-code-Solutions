class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {str(i):alpha[i-1]  for i in range(1,27)}
        i = len(s) -1
        arr = []
        while i > -1:
            if s[i] == '#':
                arr.append(d[s[i-2:i]])
                i -= 3
            else:
                arr.append(d[s[i]])
                i -= 1
        arr = arr[::-1]
        return ''.join(arr)
