# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        def recur(root):
            if root:
                recur(root.right)
                root.val = self.val = root.val + self.val
                recur(root.left)
                
        recur(root)
        return root