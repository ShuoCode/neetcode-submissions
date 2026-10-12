# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, currSum):
            # current node is null, this is base case
            if not node:
                return False

            # current node is not null
            currSum += node.val

            # current node is leaf node
            if not node.left and not node.right: 
                return currSum == targetSum

            # current node is not leaf node
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        
        currSum = 0
        return dfs(root, currSum)