# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # use DFS to get height and its balance situation
        # whether a binary tree is height-balanced ==
        # heights of left/right subtree differs no more than 1
        # so we need height of left/right subtree
        # but one more thing worth to note is that:
        # heights of left/right subtree equals to each other
        # doesn't mean that left/right subtree is balanced
        # and if one of them is not balanced, then there is no point
        # to continue the judgment
        # so we need both height and whether they are balanced of 
        # left/right subtree
        # what information do current node need?
        def dfs(node):
            if not node:
                return [True, 0]
            left= dfs(node.left)
            right= dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        # Call dfs function to start process
        return dfs(root)[0]