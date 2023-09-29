class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        first = sum(arr[0:0+k])
        if first//k >= threshold: ans += 1
        for i in range(k, len(arr)):
            first = first - arr[i-k] + arr[i]
            if first//k >= threshold: ans += 1
        return ans