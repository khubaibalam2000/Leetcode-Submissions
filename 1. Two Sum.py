class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict: return [i, dict[comp]]
            dict[nums[i]] = i