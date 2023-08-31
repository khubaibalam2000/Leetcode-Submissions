class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = float('-inf')
        for i in range(len(nums)):
            mn = min(mn, nums[i])
            mx = max(mx, nums[i] - mn)

        if mx > 0: return mx
        else: return 0