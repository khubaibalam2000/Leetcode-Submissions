# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryToDecimal(self, binary):
     
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return (decimal)
        
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        nums = []
        t = []
        def recur(root):
            if root:
                if not root.left and not root.right:
                    t.append(root.val)
                    temp = list(t)
                    nums.append(temp)
                    t.pop()
                t.append(root.val)
                recur(root.left)
                recur(root.right)
                t.pop()
                
        recur(root)
        s = []
        for i in range(len(nums)):
            sho = [str(elem) for elem in nums[i]]
            s.append(int(''.join(sho)))
        
        ans = []
        for i in range(len(s)):
            ans.append(self.binaryToDecimal(s[i]))
        return sum(ans)