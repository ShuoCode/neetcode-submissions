class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        count = 0
        dif = [[1, 0], [-1, 0], [0, 1], [0,-1]]

        def bfs(r: int, c: int):
            # find and mark all cells in a newly found island with bfs
            q = deque()            
            q.append((r, c))
            grid[r][c] = '0'

            while len(q) > 0:
                for _ in range(len(q)):
                    cr, cc = q.popleft()
                    for rdif, cdif in dif:
                        nr = cr + rdif
                        nc = cc + cdif
                        if 0 <= nr < row \
                            and 0 <= nc < col \
                            and grid[nr][nc] == '1':
                            
                            q.append((nr, nc))
                            grid[nr][nc] = '0'
            return

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)

        return count