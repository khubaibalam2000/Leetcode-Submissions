class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = l + (r - l) // 2
            capacity = 0
            td = 0
            for i in range(len(weights)):
                capacity += weights[i]
                if capacity > m:
                    capacity -= weights[i]
                    td += 1
                    capacity = weights[i]
            if td < days:
                r = m - 1
            else:
                l = m + 1
        return l