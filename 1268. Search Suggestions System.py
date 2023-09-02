class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()
        for i in range(len(searchWord)):
            temp = []
            cn = 0
            for j in products:
                
                if cn < 3 and j.startswith(searchWord[:i+1]): 
                    temp.append(j)
                    cn += 1
            ans.append(temp)
        return ans