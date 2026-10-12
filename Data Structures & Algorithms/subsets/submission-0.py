class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # decision tree: whether add each element or not
        # leaf nodes are all the subsets
        
        res = []
        subset = []

        # use index i as current element to be determined
        # whether to be added to subsets or not
        # traverse the tree using dfs and construct subsets along the way
        def dfs(i):
            # base case: it reached leaf node of this decision tree
            if i >= len(nums):
                # copy() is necessary, otherwise res will change when subset changes
                res.append(subset.copy())
                return
            
            # if it has not reached leaf node
            # then there are two choices: 
            # 1.0 add nums[i] to subsets
            subset.append(nums[i])
            # 1.1 continue constructing subsets by going deeper along the tree
            # calling the following setence means that
            # next step is to construct subsets w/ or w/o next elements in nums[] based on current decision of adding nums[i]
            dfs(i + 1)

            # 2.0 not add sums[i] to subsets
            subset.pop()
            # 2.1 same as 1.1
            dfs(i + 1)

            return res

            # the above two dfs() constructing all subsets along the decision tree based on different decision its prior step made, so each call of dfs() based on a different subset, and it reaches different final subset eventually. all we need to do is to add these unique subsets to final result list. 

        # start of constructing subsets using a decision tree
        return dfs(0)