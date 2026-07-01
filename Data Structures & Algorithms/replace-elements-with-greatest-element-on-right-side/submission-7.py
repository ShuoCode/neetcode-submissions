class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            res[i] = rightMax
            rightMax = max(rightMax, arr[i])
        return res