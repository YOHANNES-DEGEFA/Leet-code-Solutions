class FrequencyTracker:

    def __init__(self):
        self.val = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.val[number]+=1
        if self.val[number]==1:
            self.freq[1]+=1
            return 
        self.freq[self.val[number]-1]-=1
        self.freq[self.val[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.val[number]:
            self.val[number]-=1
            self.freq[self.val[number]+1]-=1
            self.freq[self.val[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)