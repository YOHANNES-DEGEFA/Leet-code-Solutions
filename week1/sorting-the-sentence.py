class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        arr = ['']*(len(s))

        for word in s: 
            arr[int(word[-1])-1] = word[:-1]

        return ' '.join(arr)
        