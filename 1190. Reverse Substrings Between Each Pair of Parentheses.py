class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] != '(' and s[i] != ')':
                stack.append(s[i])
            elif s[i] == ')':
                s2 = ''
                while stack[-1] != '(':
                    s2 += stack.pop()
                stack.pop()
                arr = list(s2)
                stack.extend(arr)
            i+=1
        return ''.join(stack)