class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # key: how to construct this decision tree
        # the essential of the combiantion in this problem is:
        # how many times of each element is included in the result

        res = []

        # i: on which element are we looking at
        # curComb: current combination
        # sum: sum of curComb
        def dfs(i, curComb, sum):
            # base cases:
            if sum == target:
                res.append(curComb.copy())
                return
            
            if i >= len(nums) or sum > target:
                return

            # other cases:
            # two choices: 
            # 1. still chose current element
            curComb.append(nums[i])
            dfs(i, curComb, sum + nums[i])
            # 2. give up adding more current element anymore
            curComb.pop() 
            dfs(i + 1, curComb, sum)

        curComb = []
        dfs(0, curComb, 0)
        return res