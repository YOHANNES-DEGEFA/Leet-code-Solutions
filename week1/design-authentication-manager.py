
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.auth = collections.defaultdict()
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        expireTime = currentTime+ self.ttl
        self.auth[tokenId] =expireTime


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.auth:
            timeToExpire = self.auth[tokenId]

            if timeToExpire > currentTime:
                self.auth[tokenId] = (currentTime+self.ttl)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        deletion_que = collections.deque()
        liveCount = 0
        for k, v in self.auth.items():
            if v <= currentTime:
        
                deletion_que.append(k)
            else:
                liveCount+=1

        for k in deletion_que:
            self.auth.pop(k)

        return liveCount



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)