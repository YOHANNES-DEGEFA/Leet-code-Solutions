class Solution:
    def sumOfThree(self, num: int) -> List[int]:

      start =  num //3 - 7    # -7 is just a random number to make the code consistent
      b, c = start +1 , start + 2 

      for a in range(start,num//2 + 5):
          curSum = a + b + c
          if curSum  == num:
              return [a,b,c]
          elif curSum > num:
               return []
          b += 1
          c += 1 

      return []




    # Moral of the Question: 
    # Any number that is divisible by 3 can be represented as the sum of three consequentive numbers 

    # Others Solution:
    """
        class Solution:
            def sumOfThree(self, num: int) -> List[int]:
                if(num%3 == 0):
                    num//= 3
                    return [num-1, num, num+1]
                return [] 
    """



        