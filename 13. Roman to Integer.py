class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        c = 0
        i = 0
        while i < len(s)-1:
            if dict[s[i]] >= dict[s[i+1]]:
                c += dict[s[i]]
                i += 1
            elif dict[s[i]] < dict[s[i+1]]:
                c += dict[s[i+1]] - dict[s[i]]
                i += 2
        if i + 1 == len(s):
            c+= dict[s[i]]
        return c