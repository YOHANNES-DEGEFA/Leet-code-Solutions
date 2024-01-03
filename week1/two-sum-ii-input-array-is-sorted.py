class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        cur = 1001
        while True: 
            cur = numbers[l] + numbers[r]
            if cur > target: 
                r -= 1 
            elif cur < target: 
                l += 1 
            else: 
                return [l+1, r+1]
        