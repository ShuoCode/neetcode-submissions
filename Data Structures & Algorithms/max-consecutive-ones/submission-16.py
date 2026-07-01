class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, result = 0, 0 
        # directly use the value in the array
        # rather than use index
        for num in nums:
            if num == 1:
                counter += 1
            else:
                result = max(counter, result)
                counter = 0
        # the wrapping up update of of the result
        # can be moved into return,
        # rather than having it in a separate if-else 
        return max(result, counter)