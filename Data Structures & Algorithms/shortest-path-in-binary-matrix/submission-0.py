from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        queue = deque()
        visit = set()

        queue.append((0, 0, 1))
        visit.add((0, 0))

        while queue:
            r, c, length = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return length

            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                    continue

                queue.append((r + dr, c + dc, length + 1))
                visit.add((r + dr, c + dc))

        return -1