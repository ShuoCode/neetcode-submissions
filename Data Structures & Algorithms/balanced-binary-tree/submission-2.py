# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getHeight(node):
            if not node:
                return 0
            lH = getHeight(node.left)
            rH = getHeight(node.right)
            if -1 <= lH - rH <= 1:
                return max(lH, rH) + 1
            else:
                return False
        
        lHeight = getHeight(root.left)
        rHeight = getHeight(root.right)
        
        return True if -1 <= lHeight - rHeight <= 1 else False

        