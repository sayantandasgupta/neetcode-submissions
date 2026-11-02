from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        if len(queue) == 0:
            return -1
        
        print(queue)
        minutes = -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or grid[r + dr][c + dc] == 0 or grid[r + dr][c + dc] == 2:
                    continue
                
                grid[r + dr][c + dc] = 2
                queue.append((r + dr, c + dc))
            
            minutes += 1
            print(queue, minutes)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes