class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            maxElement = arr[i+1]
            for j in range(i + 2, len(arr)):
                arr[i] = max(maxElement, arr[j])
        arr[len(arr) - 1] = -1
        return arr
                