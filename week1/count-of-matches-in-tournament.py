class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0 
        while n > 0:
            matches += n//2
            n = n//2 + 1 if n % 2 == 1 else n //2
            if n == 1: break
        return matches

    