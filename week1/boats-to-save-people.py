class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = len(people)

        l, r = 0, ans -1 
        while l < r: 
            cur_sum = people[l] + people[r]
            if cur_sum <= limit: 
                ans -=1 
                l += 1 
                r -= 1 
            elif cur_sum >limit: 
                r -= 1 
            else:  # i.e if the sum is less than cur_sum 
                l += 1 

        return ans 
        