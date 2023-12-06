class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s1, s2, p = [], [], []
        for n in nums: 
            if n < pivot: s1.append(n)
            elif n > pivot: s2.append(n)
            else: p.append(n)

        answer = s1 + p + s2 
        return answer