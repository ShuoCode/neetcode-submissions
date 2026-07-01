class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # because there are two types of elements, one equals val, one not
        # so we need two pointers for each of them
        # one starts from the beginning of the array
        # only goes forward when this one is the element we are requiring
        # the other one starts from the end of the array
        # goes back when it is placed a not want element
        # in this way, it doesn't need to go through the whole array
        k = 0
        n = len(nums)
        while k < n:#
            if nums[k] == val:
                tmp = nums[k] 
                nums[k] = nums[n-1]
                nums[n-1] = tmp
                n -= 1
                if nums[k] != val:
                    k += 1
                continue
            k += 1
        return k