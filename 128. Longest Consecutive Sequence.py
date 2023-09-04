class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 1: return 1
        if len(nums) == 2 and (nums[0] != nums[1] + 1 and nums[0] != nums[1] - 1): return 1
        if len(nums) == 2 and (nums[0] == nums[1] + 1 or nums[0] == nums[1] - 1): return 2
        if not nums: return 0
        sets = set(nums)
        nums = list(sets)
        c = 1
        gm = 1
        for i in range(len(nums)):
            t = nums[i]
            if t - 1 in sets:
                sets.remove(t)
                while t - 1 in sets:
                    t -= 1
                    c += 1
                    sets.remove(t)
                t = nums[i]
                while t + 1 in sets:
                    t += 1
                    c += 1
                    sets.remove(t)
            gm = max(c, gm)
            c = 1
        return gm