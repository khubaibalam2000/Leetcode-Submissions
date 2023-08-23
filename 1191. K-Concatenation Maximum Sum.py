class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def Kadane(arr):
            lm = gm = arr[0]
            for i in range(1, len(arr)):
                lm = max(arr[i], arr[i] + lm)
                gm = max(lm,gm)

            if gm > 0:
                return gm
            else:
                return 0
        
        if k == 1:
            return Kadane(arr)
        temp = list(arr)
        for i in range(1):
            for j in range(len(temp)):
                arr.append(temp[j])
        if sum(arr) < 0:
            return Kadane(arr)
        else:
            gg = Kadane(arr)
            gg += (k-2) * sum(temp)
            return gg%(10**9 + 7)