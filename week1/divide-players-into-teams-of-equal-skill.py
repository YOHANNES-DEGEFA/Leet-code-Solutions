class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        coma = sum(skill)
        division = len(skill)//2
        target = coma//division
        skill.sort()
        ans = 0 
        l, r = 0, len(skill)-1

        while l < r: 
            if skill[l] + skill[r] != target: 
                return -1 
            ans += skill[l]*skill[r]
            l += 1 
            r -= 1

        return ans 

        