class Solution:
    def totalMoney(self, n: int) -> int:
        coma = n//7
        rem = n%7
        week_tracker = 1
        total_sum = 0
        for i in range(coma):
            for j in range(week_tracker,week_tracker+7):
                total_sum +=j
            week_tracker +=1
        for j in range(week_tracker,rem+week_tracker):
            total_sum +=j
        return total_sum
