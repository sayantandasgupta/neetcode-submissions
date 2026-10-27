class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
        
        visit = [False] * numCourses

        def dfs(node):
            if visit[node]:
                return False
            if adj[node] == []:
                return True
            
            visit[node] = True
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visit[node] = False
            adj[node] = []
            return True

        for u in range(numCourses):
            if not dfs(u):
                return False

        return True