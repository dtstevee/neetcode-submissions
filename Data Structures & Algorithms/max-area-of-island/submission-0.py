class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rlen = len(grid)
        clen = len(grid[0])
        visit = set()


        def dfs(grid, r, c):

            if min(r,c) < 0 or r == rlen or c == clen:
                return 0
            
            if grid[r][c] != 1:
                return 0
            
            if (r,c) in visit:
                return 0
            
            visit.add((r,c))
            
            area = 1
            area += dfs(grid, r+1, c)
            area += dfs(grid, r-1, c)
            area += dfs(grid, r, c+1)
            area += dfs(grid, r, c-1)

            return area
        
        result = []
        for r in range(rlen):
            for c in range(clen):
                area_size = dfs(grid, r, c)
                result.append(area_size)
        
        return max(result)