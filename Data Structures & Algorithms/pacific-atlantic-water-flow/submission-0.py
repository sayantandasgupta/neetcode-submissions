class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac = set()
        atl = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visit, prevHeight):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)
        
        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)
        
        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result

