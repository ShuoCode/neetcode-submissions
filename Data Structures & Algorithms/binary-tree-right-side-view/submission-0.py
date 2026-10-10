# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # right side view nodes of a tree is essentially
        # right most nodes of each level
        # so we need to traverse the tree in level order
        # and record the rightmost nodes of each level
        res = []

        if not root:
            return []
        
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if i == qLen - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return res