class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in dict: dict[groupSizes[i]].append(i)
            else: dict[groupSizes[i]] = [i]

        ans = []
        for key, value in dict.items():
            N = len(value)//key
            ans.append([value[(i*len(value))//N:((i+1)*len(value))//N] for i in range(N)])

        res = []
        for i in ans:
            for j in i:
                res.append(j)
        return res