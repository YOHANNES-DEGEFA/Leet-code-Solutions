class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination: 
            return 0
        if start > destination:
            start, destination = destination, start 

        d1 = sum(distance[start:destination])
    
        d3 = sum(distance[0:start])  + sum(distance[destination:])
        answer = min(d1,d3)
        return answer 
        
        