class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0
        for index in range(len(nums)):
            if index < len(nums) - 1:
                if nums[index] == 1:
                    counter += 1
                else:
                    if counter >= result:
                        result = counter
                    counter = 0
            else:
                if nums[index] == 1:
                    counter += 1
                if counter >= result:
                    result = counter
        
        return result