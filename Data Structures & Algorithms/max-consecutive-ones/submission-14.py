class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, result, length = 0, 0, len(nums)
        for index in range(length):
            if nums[index] == 1:
                counter += 1
            if nums[index] == 0 or index == length - 1:
                result = max(counter, result)
                counter = 0
        return result