class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,'IV':4,"IX":9,"XL":40,'XC':90,"CD":400,"CM":900}

        answer = 0 
        for i in range(len(s)): 
            if i + 1 < len(s):
                if hashMap[s[i]] >= hashMap[s[i+1]]:
                    answer += hashMap[s[i]]
                else:
                    answer -= hashMap[s[i]]
            else:
                answer += hashMap[s[i]]
                
        return answer 
        