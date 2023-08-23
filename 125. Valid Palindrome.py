class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        r = ''
        for i in s:
            if i.isalnum(): r += i
        return r == r[::-1]