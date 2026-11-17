class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIMS = len(grid)
        if grid[0][0] or grid[DIMS - 1][DIMS - 1]:
            return -1
            
        visited = set()
        q = deque()
        q.append((0,0))
        visited.add((0,0))
        length = 0
        direct = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

        while q:
            length += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == c == DIMS - 1:
                    return length
                
                for dr, dc in direct:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 \
                        or nr >= DIMS or nc >= DIMS \
                        or (nr, nc) in visited \
                        or grid[nr][nc] == 1:

                        continue
                
                    q.append((nr, nc))
                    visited.add((nr, nc))

        return -1