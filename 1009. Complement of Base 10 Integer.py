class Solution:
    def bitwiseComplement(self, n: int) -> int:   
        def setBit(n):
            set = 0
            n //= 2
            while n > 0:
                n //=2
                set += 1
            return 1 << set
        return n^((setBit(n)<<1)-1)