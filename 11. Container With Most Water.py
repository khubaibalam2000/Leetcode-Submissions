class Solution:
    def maxArea(self, height: List[int]) -> int:
        nums = []
        i = 0
        j = len(height) - 1
        while i != j:
            nums.append(abs(min(height[i], height[j])*i-min(height[i], height[j])*j))
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        
        return max(nums)