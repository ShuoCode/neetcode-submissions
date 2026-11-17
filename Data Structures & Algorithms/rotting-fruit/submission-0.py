class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        cntFresh = 0 # 1
        cntRotten = 0 # 2
        time = 0

        # rotten fruit: 2
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    cntFresh += 1
                if grid[r][c] == 2:
                    cntRotten += 1
                    q.append((r, c))

        if cntFresh == 0:
            return 0
        if cntRotten == 0:
            return -1

        
        while q:
            time += 1
            # precess rotten fruits
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in direct:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS \
                        and grid[nr][nc] == 1:

                        grid[nr][nc] = 2
                        q.append((nr, nc))

                        cntFresh -= 1
                        if cntFresh == 0:
                            return time
            
        return -1