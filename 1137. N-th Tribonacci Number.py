class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1]*n
        def recur(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if dp[n-1] != -1:
                return dp[n-1]
            dp[n-1] = recur(n-1) + recur(n-2) + recur(n-3)
            return dp[n-1]
        
        return recur(n)