class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        return ''.join(stack)