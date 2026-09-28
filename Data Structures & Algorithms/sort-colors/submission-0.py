class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket Sort
        arr = [0] * 3
        for n in range(len(nums)):
            arr[nums[n]] += 1

        k = 0
        for i in range(len(arr)):
            for j in range(arr[i]):
                nums[k] = i
                k += 1
