class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hashMap = {}
        result = 0 

        #Block 1: map numbers with their indices
        for i, num in enumerate(nums):
            if num in hashMap: 
                hashMap[num].append(i)
            else: 
                hashMap[num] = [i]

        #Block 2: function to calculate the number of indices that
        # are divisisible by k  

        def calcIdxProdDivsblebyK(indices):
            n = len(indices)
            count = 0 

            # n-1 cause there is no element next to pairs[n-1] element
            for i in range(n-1): 
                for j in range(i+1,n):
                    if (indices[i]*indices[j]) %k == 0: 
                        count += 1 

            return count 

        
        #Block 3: One more traversal to find our result 
        nums = list(set(nums))
        for num in nums: 
            if len(hashMap[num]) > 1: 
                result += calcIdxProdDivsblebyK(hashMap[num])

        return result 



      

        