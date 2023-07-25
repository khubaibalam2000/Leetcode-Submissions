# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = -1
        def recur(root, mina, maxa):
            if root:
                mina = min(mina, root.val)
                maxa = max(maxa, root.val)
                self.maxDiff = max(self.maxDiff, abs(mina-maxa))
                recur(root.left, mina, maxa)
                recur(root.right, mina, maxa)
        
        recur(root, root.val, root.val)
        return self.maxDiff