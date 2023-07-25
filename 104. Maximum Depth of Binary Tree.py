# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(root, height):
            if root:
                return max(recur(root.right, height+1), recur(root.left, height+1))
            return height
        
        return recur(root, 0)