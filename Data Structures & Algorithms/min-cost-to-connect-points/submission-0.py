import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([j, weight])
                adj[j].append([i, weight])
        
        minHeap = [[0, 0]]
        visit = set()
        res = 0
        while len(visit) < n:
            weight, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            res += weight
            visit.add(n1)
            for neighbor, weight in adj[n1]:
                heapq.heappush(minHeap, [weight, neighbor])

        return res