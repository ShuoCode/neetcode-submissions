class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        visited = set()
        row = len(grid)
        col = len(grid[0])

        def dfs(r: int, c: int, area: int):
            if r >= row or r < 0 \
                or c >= col or c < 0 \
                or (r, c) in visited \
                or grid[r][c] == 0:

                return 0

            visited.add((r, c))

            return 1 + dfs(r + 1, c, area) + dfs(r, c + 1, area) + dfs(r - 1, c, area) + dfs(r, c - 1, area)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    result = max(dfs(i, j, 0), result)

        return result