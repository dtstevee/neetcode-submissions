class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        rows, cols = len(heights), len(heights[0])
        
        pacific = [(0,i) for i in range(cols)] + [(i,0) for i in range(rows)]
        atlantic = [(rows-1,i) for i in range(cols)] + [(i,cols-1) for i in range(rows)]

        def bfs(start):
            visted = set(start)
            queue = deque(start)
            
            while queue:
                r,c = queue.popleft()
                direction = [(1,0),(-1,0),(0,1),(0,-1)]

                for dr,dc in direction:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and heights[nr][nc] >= heights[r][c]
                        and (nr,nc) not in visted):
                        visted.add((nr,nc))
                        queue.append((nr,nc))
            return visted
        
        pacific_mid = bfs(pacific)
        atlantic_mid = bfs(atlantic)
        
        result = []
        for i in pacific_mid:
            if i in atlantic_mid:
                result.append(list(i))
        return result

        