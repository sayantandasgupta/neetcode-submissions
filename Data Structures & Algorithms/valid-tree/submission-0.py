class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        numEdges = len(edges)

        return numEdges == n - 1