import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}

        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]

            adj[u].append([v, w])
            adj[v].append([u, w])
        
        
        minHeap = [(-1, start_node)]
        visit = set()

        while minHeap:
            prob, cur = heapq.heappop(minHeap)
            visit.add(cur)

            if cur == end_node:
                return -prob
            
            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(minHeap, (prob * edgeProb, nei))

        return 0.00
        
