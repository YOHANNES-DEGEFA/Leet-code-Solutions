class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        answer = []
        def calculateMinIdxSum(boxes,cur_idx):

            minIdxSum = 0
            # find all the '1's that found to the right 
            for i in range(cur_idx,len(boxes)):
                if boxes[i] == '1':
                    minIdxSum += abs(i-cur_idx)

            # find '1' that found to the left
            for j in range(0, cur_idx):
                if boxes[j] == '1':
                    minIdxSum += abs(j-cur_idx)


            return minIdxSum 

        for i in range(len(boxes)):
            cur_ans = calculateMinIdxSum(boxes,i)
            answer.append(cur_ans)


        return answer




        