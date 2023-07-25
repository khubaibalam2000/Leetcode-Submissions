# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def recur(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and recur(node1.left, node2.right) and recur(node1.right, node2.left)
            if (node1 and not node2) or (not node1 and node2):
                return False
            return True
        return recur(root.left, root.right)