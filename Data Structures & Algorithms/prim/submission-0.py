import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])

        minHeap = [[0, 0]]
        res = 0
        visit = set()

        while minHeap and len(visit) < n:
            weight, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)
            res += weight

            for neighbor, w in adj[node]:
                heapq.heappush(minHeap, [w, neighbor])

        return res if len(visit) == n else -1
