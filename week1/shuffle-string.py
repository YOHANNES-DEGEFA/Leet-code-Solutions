class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        chars = [n for n in indices]
        for i, c in zip(indices, s):
            chars[i] = c

        return ''.join(chars)