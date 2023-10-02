class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = -1
        b = -1
        c = -1
        ans = 0
        for i in range(len(s)):
            if s[i] == 'a': a = i
            elif s[i] == 'b': b = i
            elif s[i] == 'c': c = i
            if a == -1 or b == -1 or c == -1: continue
            ans += min(a,b,c) + 1
        
        return ans