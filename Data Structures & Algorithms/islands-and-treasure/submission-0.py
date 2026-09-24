class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        rows,cols = len(grid), len(grid[0])
        queue = deque()

        # record all treasure location, find all treasure, then do BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            ri, ci = queue.popleft()
            direction = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in direction:
                nr = ri + dr
                nc = ci + dc
                if (0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[ri][ci] + 1
                    queue.append((nr,nc))
                
            
        