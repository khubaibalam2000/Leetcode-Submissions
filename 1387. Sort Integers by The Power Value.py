class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = {}
        dp = {}
        def recur(el, c, orig):
            if el == 1:
                return c
            
            if el in dp:
                return dp[el] + c
            
            elif el % 2 == 0:
                temp = recur(int(el/2), c+1, orig)
                dp[el] = temp - c
                return temp
            elif el % 2 != 0:
                temp = recur(el*3+1, c+1, orig)
                dp[el] = temp - c
                return temp
            
        
        for i in range(lo, hi+1):
            if i == 1:
                dp[i] = 0
            recur(i, 0, i)
            
        for i in range(lo, hi+1):
            nums[i] = dp[i]
        nums = sorted(nums.items(), key=lambda x: x[1])
        return nums[k-1][0]