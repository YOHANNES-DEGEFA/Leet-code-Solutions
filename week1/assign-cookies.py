class Solution:
    def findContentChildren(self, preference: List[int], size: List[int]) -> int:
        preference.sort();      size.sort(); 
        pl, al = len(preference), len(size)
        i = j = max_content = 0 

        while i < pl and j < al:
            if preference[i] > size[j]:
                j += 1 
            else: 
                max_content += 1 
                i += 1 
                j += 1 

        return max_content 




