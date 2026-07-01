class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        res[n - 2] = arr[n - 1]
        for i in range(n - 3, -1, -1):
            res[i]= max(res[i+1], arr[i+1])
        return res

