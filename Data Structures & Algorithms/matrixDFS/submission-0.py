class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visited):
            rows, cols = len(grid), len(grid[0])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == 1:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1

            visited.add((r, c))

            count = 0

            for dr, dc in directions:
                count += dfs(grid, r + dr, c + dc, visited)
            
            visited.remove((r, c))

            return count

        visited = set()

        return dfs(grid, 0, 0, visited)
