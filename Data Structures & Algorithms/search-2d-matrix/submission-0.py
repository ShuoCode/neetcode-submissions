class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        top = 0
        bot = row - 1

        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        if top > bot:
            return False

        l = 0
        r = col - 1

        while l <= r:
            num = (l + r) // 2
            if target < matrix[mid][num]:
                r = num - 1
            elif target > matrix[mid][num]:
                l = num + 1
            else:
                return True

        return False