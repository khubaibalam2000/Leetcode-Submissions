# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (1e9, -1e9, 0, True)
            ll, lh, ls, lv = dfs(node.left)
            rl, rh, rs, rv = dfs(node. right)
            v = lv and rv and node.val> lh and node.val<rl
            s = ls + rs + node.val if v else -1
            self.ans = max(self.ans, s)
            return (min(ll, node.val), max(rh, node.val), s, v)
        self.ans = 0
        dfs(root)
        return self.ans