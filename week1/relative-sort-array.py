class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        temp = []
        for n in arr2: 
            for n2 in arr1: 
                if n2 == n: 
                    ans.append(n)

        arr2 = set(arr2)
        
        for n in arr1: 
            if n not in arr2:
                temp.append(n)
        temp.sort()
        ans += temp
        return ans 
        