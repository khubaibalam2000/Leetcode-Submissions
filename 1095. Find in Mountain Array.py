# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPeak():
            l = 0
            r = mountain_arr.length() - 1
            while l<r:
                m = (l+r)//2
                if mountain_arr.get(m) < mountain_arr.get(m+1):
                    l = m + 1
                else:
                    r = m

            return l
            
        peak = findPeak()
        def binarySearchBeforePeak(l, r):
            while l <= r:
                m = l + (r-l)//2
                if mountain_arr.get(m) == target: return m
                elif mountain_arr.get(m) < target: l = m + 1
                else: r = m - 1

        def binarySearchAfterPeak(l, r):
            while l <= r:
                m = l + (r-l)//2
                if mountain_arr.get(m) == target: return m
                elif mountain_arr.get(m) > target: l = m + 1
                else: r = m - 1
        
        idx = binarySearchBeforePeak(0, peak)
        if idx is not None: return idx
        else: 
            idx = binarySearchAfterPeak(peak+1, mountain_arr.length()-1)
            if idx is not None: return idx
        return -1