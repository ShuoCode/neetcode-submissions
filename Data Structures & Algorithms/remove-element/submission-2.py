class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cntVal = 0
        for i in range(len(nums)):
            if nums[i] != val:
                cntVal += 1
            else:
                for j in range(i + 1, len(nums)):
                    if nums[j] != val:
                        cntVal += 1
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
                        break
        return cntVal




                

