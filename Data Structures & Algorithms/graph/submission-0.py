class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        return self.dfs(src, dst, visit)
    
    def dfs(self, node: int, target: int, visit: set) -> bool:
        if node in visit:
            return False
        if node == target:
            return True

        visit.add(node)
        for neighbour in self.graph[node]:
            if self.dfs(neighbour, target, visit):
                return True
        
        return False