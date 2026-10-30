class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False] * n

        def dfs(node):
            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)

        count = 0

        for u in range(n):
            if not visit[u]:
                dfs(u)
                count += 1

        return count