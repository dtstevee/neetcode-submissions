class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit_hash = set()
        rlen = len(grid)
        clen = len(grid[0])
        count = 0

        def dfs(grid, r, c):
            if min(r,c) < 0 or r == rlen or c == clen:
                return
            
            if grid[r][c] != '1':
                return
            
            if (r,c) in visit_hash:
                return
            
            visit_hash.add((r,c))

            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)

        for r in range(rlen):
            for c in range(clen):
                if (r,c) not in visit_hash and grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        
        return count
