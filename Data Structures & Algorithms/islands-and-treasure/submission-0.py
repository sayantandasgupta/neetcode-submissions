from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 1))
                    visit.add((r, c))

        while queue:
            for i in range(len(queue)):
                r, c, l = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visit or grid[nr][nc] == -1:
                        continue
                    
                    grid[nr][nc] = l
                    queue.append((nr, nc, l + 1))
                    visit.add((nr, nc))

        return
                


