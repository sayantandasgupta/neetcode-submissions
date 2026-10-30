class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
        
        result = []
        visit = [False] * numCourses
        cycle = [False] * numCourses

        def dfs(node):
            if cycle[node]:
                return False
            if visit[node]:
                return True
            
            cycle[node] = True
            for neighbor in adj[node]:
                if dfs(neighbor) == False:
                    return False
            
            cycle[node] = False
            visit[node] = True
            result.append(node)
            return True
        
        for u in range(numCourses):
            if dfs(u) == False:
                return []

        return result