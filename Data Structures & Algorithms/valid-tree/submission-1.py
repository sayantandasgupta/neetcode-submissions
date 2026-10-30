class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False] * n
        
        def dfs(node, parent):
            if visit[node]:
                return False
            
            visit[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and sum(visit) == n
