# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return root
        nums = []
        t = []
        def recur(root):
            if root:
                if not root.left and not root.right:
                    t.append(root.val)
                    temp = list(t)
                    nums.append(sum(temp))
                    t.pop()
                t.append(root.val)
                recur(root.left)
                recur(root.right)
                t.pop()
                
        recur(root)
        for i in range(len(nums)):
            if nums[i] == targetSum:
                return True
        return False