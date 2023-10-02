class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        sor = sorted(nums)
        for i in range(len(nums)):
            ans.append(sor.index(nums[i]))
        return ans