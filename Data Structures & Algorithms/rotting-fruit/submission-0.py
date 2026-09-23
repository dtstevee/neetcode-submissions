class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        mins = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                ri,ci = queue.popleft()
                direction = [(1,0),(-1,0), (0,1),(0,-1)]
                for dr, dc in direction:
                    nr = ri + dr
                    nc = ci + dc
                    
                    if (0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
            mins += 1
        return mins if fresh == 0 else -1