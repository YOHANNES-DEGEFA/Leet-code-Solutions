class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sp = set(spaces)
        ans = []
        for i, c in enumerate(s):
            if i in sp:
                ans.append(' ')
            ans.append(c)
        res =  "".join(ans)
        return res