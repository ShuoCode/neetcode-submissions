class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # We only care about how many elements we can find
        # when iterates the whole array
        nextAvailablePosition = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nextAvailablePosition] = nums[i]        
                nextAvailablePosition += 1
        return nextAvailablePosition
        

        