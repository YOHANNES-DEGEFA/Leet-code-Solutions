class Bitset:

    def __init__(self, size: int):
        self.zeroes = ["0"] * size
        self.ones = ["1"] * size
        self.count_1 = 0

    def fix(self, idx: int) -> None:
        if self.zeroes[idx] != "1":
            self.zeroes[idx] = "1"
            self.ones[idx] = "0"
            self.count_1 += 1

    def unfix(self, idx: int) -> None:
        if self.zeroes[idx] != "0":
            self.zeroes[idx] = "0"
            self.ones[idx] = "1"
            self.count_1 -= 1

    def flip(self) -> None:
        self.zeroes, self.ones = self.ones, self.zeroes
        self.count_1 = len(self.zeroes) - self.count_1

    def all(self) -> bool:
        return len(self.zeroes) == self.count_1

    def one(self) -> bool:
        return self.count_1 > 0

    def count(self) -> int:
        return self.count_1

    def toString(self) -> str:
        return "".join(self.zeroes)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()