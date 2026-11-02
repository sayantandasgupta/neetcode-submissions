class DSU:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        rank1, rank2 = self.rank[p1], self.rank[p2]

        if p1 == p2:
            return False

        if rank1 > rank2:
            self.par[p2] = p1
        elif rank1 < rank2:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        dsu = DSU(len(edges))

        for n1, n2 in edges:
            if not dsu.union(n1, n2):
                return [n1, n2]
        
        return [n1, n2]