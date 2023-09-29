class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict = {}
        for i in arr:
            if i in dict: dict[i] += 1
            else: dict[i] = 1

        freqs = list(dict.values())
        freqs.sort(reverse = True)
        total = len(arr)//2
        c = 0
        ans = 0
        for i in freqs:
            c += i
            ans += 1
            if c >= total: return ans