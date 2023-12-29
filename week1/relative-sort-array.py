class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2ToIdx = {}
        elem = set(arr2)

        N = len(arr1)
        for i, n in enumerate(arr2): 
            arr2ToIdx[n] = i 

        def comparator(n):
            if n not in elem: 
                return n + N 
            return arr2ToIdx[n]

        arr1.sort(key=comparator)
        return arr1