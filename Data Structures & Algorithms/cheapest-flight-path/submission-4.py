from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float("INF")]*n
        dist[src] = 0

        for i in range(k+1):
            tmp = dist.copy()
            for u,v,w in flights:
                if tmp[u] == float("INF"):
                    continue
                if tmp[v] > dist[u]+w:
                    tmp[v] = dist[u]+w
            dist = tmp
        return -1 if dist[dst] == float("INF") else dist[dst]   




