class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                arr[i] = max(arr[i], arr[j])
        arr[len(arr) - 1] = -1
        return arr
                