class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for i in range(len(arr)):
            if arr[i] in dict:
                dict[arr[i]] += 1
                continue
            dict[arr[i]] = 1
        
        values = dict.values()
        return len(values) == len(set(values))