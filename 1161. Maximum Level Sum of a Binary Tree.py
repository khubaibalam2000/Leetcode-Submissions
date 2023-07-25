# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        ans=[]
        q= deque([root])
        while q:
            currLevel=[]
            for _ in range(len(q)):
                node= q.popleft()
                currLevel.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
            ans.append(sum(currLevel))
        maxo = max(ans)
        for i in range(len(ans)):
            if maxo == ans[i]: return i + 1