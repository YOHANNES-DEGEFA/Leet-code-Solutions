class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        i = j = 0 
        m, n = len(list1), len(list2)
        result = []

        while i < m and j < n: 
            start = max(list1[i][0], list2[j][0])
            end = min(list1[i][1], list2[j][1])

            if start <= end: 
                result.append([start,end])

            if list1[i][1] < list2[j][1]: 
                i += 1 
            else: 
                j += 1 

        return result 
       
        

