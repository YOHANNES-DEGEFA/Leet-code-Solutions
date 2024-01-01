class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        d = defaultdict(list)

        for point in points: 
            x, y = point 
            distance = (x**2 + y**2) ** 0.5
            d[distance].append(point)


        temp = sorted(d.keys())
        ans = []
        for i in range(k):
            temp2 = d[temp[i]]
            for j in range(len(temp2)):
                ans.append(temp2[j])
            if len(ans) == k: 
                break
        return ans 

        