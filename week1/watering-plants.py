class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:


        curCap = capacity
        step = 1
        sumSteps = 0
        for i, num in enumerate(plants):
            if num > curCap:
                curCap = capacity 
                sumSteps += 2*i +1 
                step += 1 
            else:
                sumSteps += 1

            curCap -= num

        return sumSteps



        # self.answer = 0 
        # def rec(i,curCap,steps):

        #     if i >= len(plants):
        #         return 
        #     while i < len(plants) and plants[i] <= curCap: 
                
        #         if curCap < plants[i]:
        #             self.answer += steps
        #             return rec(i,capacity,steps+1)
        #         self.answer += steps
        #         curCap -= plants[i]
        #         i += 1 

        #     return self.answer 

        # rec(0,capacity,1)

        # return self.answer 