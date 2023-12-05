class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        pow_num1, pow_num2 = len(num1)-1, len(num2) -1 

        first_number, second_number = 0, 0 

        def stringToInt(num, pow):

            digitsList = [0,1,2,3,4,5,6,7,8,9]
            number =  0 

            for digit in num: 
                for n in digitsList: 
                    if str(n) == digit:
                        digit = n 
                        break
                
                number +=  digit * 10 ** pow

                pow -= 1

            return number 

        first_number = stringToInt(num1,pow_num1)

        second_number = stringToInt(num2, pow_num2)

        product = first_number * second_number 

        return str(product)
        
        