class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dif = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited = set()
        count = 0

        def dfs(r: int, c: int):
            if r < 0 or r >= row \
                or c < 0 or c >= col \
                or (r, c) in visited \
                or grid[r][c] == '0':
                return
            
            visited.add((r, c))
            for rdif, cdif in dif:
                dfs(r + rdif, c + cdif)
            return

        for i in range(row):
            for j in range(col):
                if (i, j) not in visited and grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count