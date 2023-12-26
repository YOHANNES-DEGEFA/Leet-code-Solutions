class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

      n  = len(names)

      for i in range(n):
          for j in range(n-1):
              if heights[j+1] > heights[j]:
                names[j], names[j+1] = names[j+1], names[j]
                heights[j], heights[j+1] = heights[j+1], heights[j]

      return names

