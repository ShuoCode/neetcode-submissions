class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = set()
        row = len(image)
        col = len(image[0])
        original_color = image[sr][sc]
        
        if image[sr][sc] == color:
            return image

        def dfs(r: int, c: int):
            if (r, c) in visited or \
                r >= row or r < 0 or \
                c >= col or c < 0 or \
                image[r][c] != original_color:
                return
            
            image[r][c] = color
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

            return
        
        dfs(sr, sc)
        return image