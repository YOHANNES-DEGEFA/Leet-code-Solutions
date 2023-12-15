class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        hash = defaultdict(int)

        for domain in cpdomains:
            s = domain.index(' ')
            num = int(domain[:s])
            hash[domain[s+1:]] += num 
            i = s+1  
            while i < len(domain):
                if domain[i] == '.':
                    hash[domain[i+1:]] += num 

                i += 1
        res = []
        for k, v in hash.items():
            wholeStr = str(v) + ' ' + k 
            res.append(wholeStr)

        return res 


        
        