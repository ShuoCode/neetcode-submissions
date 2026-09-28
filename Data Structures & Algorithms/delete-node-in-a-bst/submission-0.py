# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: 
            # When the target node has only 0 or 1 child
            # We can directly know the deleted subtree's root
            # So we can directly return it
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Find the correct value to be replaced with the root
                root.val = self.minValInBST(root.right)
                # when deleting the selected node
                # we need to remember to stitch the subtree after deletion
                # to the current tree, because the new subtree might have
                # different root
                root.right = self.deleteNode(root.right, root.val)

        return root

    def minValInBST(self, root: TreeNode) -> TreeNode:
        curr = root
        while curr.left:
            curr = curr.left
        return curr.val