class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
        for i in t:
            if i in dict and dict[i] > 0:
                dict[i] -= 1
            else:
                ans += 1
        return ans