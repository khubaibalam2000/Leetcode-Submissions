# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        nums = []
        self.totalSum = 0
        def recur(root):
            if root:
                self.totalSum = root.val + recur(root.left) + recur(root.right)
                nums.append(self.totalSum)
                return self.totalSum
            return 0
        recur(root)
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, nums[i]*(self.totalSum-nums[i]))
        return ans%(10**9+7)