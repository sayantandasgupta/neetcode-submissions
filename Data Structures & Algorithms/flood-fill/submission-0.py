class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(grid, r, c, visited, color, original_color):
            rows, cols = len(grid), len(grid[0])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] != original_color:
                return

            
            visited.add((r, c))

            grid[r][c] = color

            for dr, dc in directions:
                dfs(grid, r + dr, c + dc, visited, color, original_color)

        visited = set()
        dfs(image, sr, sc, visited, color, image[sr][sc])
        return image

            