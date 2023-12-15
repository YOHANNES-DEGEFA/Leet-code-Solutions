class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.totalCheck = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkInMap[id]
        route = (start, stationName)

        if route not in self.totalCheck: 
            self.totalCheck[route] = [0,0]
        self.totalCheck[route][0] += t-time
        self.totalCheck[route][1] += 1 
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalCheck[(startStation,endStation)]

        return total/ count 
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)