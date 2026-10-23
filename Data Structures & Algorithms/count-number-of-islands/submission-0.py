class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(grid, r, c, visit):
            rows, cols = len(grid), len(grid[0])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            if min(r,c) < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == "0":
                return

            visit.add((r, c))
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(grid, r + dr, c + dc, visit)

        rows, cols = len(grid), len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(grid, r, c, visit)
                    count += 1

        return count