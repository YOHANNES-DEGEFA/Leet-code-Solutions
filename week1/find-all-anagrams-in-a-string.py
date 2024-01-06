class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Finds all the start indices of anagrams of p 
            Args: 
                s = string from which we check the presecense of anagrams of p
                p = string whose anagram is to be find in s
            Return: 
                array of start indices of all the anagrams of p in s 
        """
        
        wordDict = [0]*26
        pl = len(p)
        answer = []

        for char in p: 
            wordDict[ord(char)-97] += 1 

        l = 0 
        for r in range(len(s)):
            
            wordDict[ord(s[r])-97] -=  1 
           
            if r-l+1 == pl: 
                if all(x==0 for x in wordDict): 
                    answer.append(l)

                wordDict[ord(s[l])-97] +=  1 
                l += 1

        return answer 