class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = float("inf")
        N = len(fronts)

        valids = {}
        for i in range(N):
            valids[fronts[i]] = True
            valids[backs[i]] = True

        for i in range(N):
            if fronts[i] == backs[i]:
                valids[fronts[i]] = False
        
        for num in valids:
            if valids[num]:
                if num < ans: 
                    ans = num 
                        
        return ans if ans != float("inf") else 0

        # goodInt = float('inf')
        # frontsMap = defaultdict(int)
        
        # for i in range(len(fronts)):
        #     frontsMap[fronts[i]] += 1 
           
        # for i in range(len(fronts)):
            
        #     if frontsMap[fronts[i]] == 1 and backs[i] != fronts[i]:
        #         goodInt = min(goodInt, fronts[i])

        #         del frontsMap[fronts[i]]
        #         frontsMap[backs[i]] += 1 

        #         fronts[i], backs[i] = backs[i], fronts[i]

        #     elif frontsMap[backs[i]] == 0:
        #         goodInt = min(goodInt, backs[i])
        #         frontsMap[backs[i]] = 1 
        #         fronts[i], backs[i] = backs[i], fronts[i]
                
        #         frontsMap[fronts[i]] -= 1

        # return goodInt if goodInt < float('inf') else 0 



