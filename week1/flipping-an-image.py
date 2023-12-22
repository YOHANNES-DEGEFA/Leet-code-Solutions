class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row, n = len(image), len(image[0])
        def flip(row, n):
           l, r = 0 , n-1

           while l < r: 
               row[l], row[r] = row[r], row[l]
               l += 1 
               r -= 1 
        def invert(row):
            for i in range(len(row)):
                row[i] = 0 if row[i] == 1 else 1


        for row in image: 
            flip(row,n)
            invert(row)

        return image
    
        