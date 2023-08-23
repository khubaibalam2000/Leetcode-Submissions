class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            
            ok = []
            for j in range(i+1):
                # nCr = n!/((n-r)!*r!)
                
                # print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
                ok.append(factorial(i)//(factorial(j)*factorial(i-j)))
            # for new line
            # print()
            ans.append(ok)
        return ans