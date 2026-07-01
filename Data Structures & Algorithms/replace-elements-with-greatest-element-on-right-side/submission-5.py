class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            rightMax = -1
            for j in range(i + 1, len(arr)):
                rightMax = max(rightMax, arr[j])
            arr[i] = rightMax
        return arr
                