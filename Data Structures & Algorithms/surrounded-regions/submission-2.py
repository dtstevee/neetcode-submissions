class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        rows,cols = len(board),len(board[0])
        queue = deque()

        for ri in range(rows):
            if board[ri][0] == 'O':
                board[ri][0] = 'T'
                queue.append((ri,0))
            if board[ri][cols - 1] == 'O':
                board[ri][cols - 1] = 'T'
                queue.append((ri, cols - 1))

        for ci in range(cols):
            if board[0][ci] == 'O':
                board[0][ci] = 'T'
                queue.append((0,ci))
            if board[rows - 1][ci] == 'O':
                board[rows - 1][ci] = 'T'
                queue.append((rows-1, ci))

        while queue:
            r,c = queue.popleft()
            direction = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr,dc in direction:
                nr = r + dr
                nc = c + dc
                
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == 'O'):
                    board[nr][nc] = 'T'
                    queue.append((nr,nc))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
