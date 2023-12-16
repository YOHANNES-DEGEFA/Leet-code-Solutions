class ATM:

    def __init__(self):
        self.bank = [0, 0, 0, 0, 0]
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.bank = [a + b for a, b in zip(self.bank, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        withdrawal = [0] * 5
        for i in range(4, -1, -1):
            withdrawal[i] = min(self.bank[i], amount // self.notes[i])
            amount -= withdrawal[i] * self.notes[i]
            if amount == 0:
                break
        
        if amount == 0:
            self.bank = [x - y for x, y in zip(self.bank, withdrawal)]
            return withdrawal
        else:
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)