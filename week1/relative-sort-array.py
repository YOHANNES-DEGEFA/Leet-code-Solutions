class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        idx_dict = {}
        for i in range(len(arr2)):
            idx_dict[arr2[i]]  = i 

        arr2 = set(arr2)
        N = len(arr1)
        def comp_by_idx(num):
            if num not in arr2: 
                return N + num 

            return idx_dict[num]

        arr1.sort(key=comp_by_idx)
        return arr1