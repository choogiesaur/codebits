from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(n+1):
            binary = bin(i)
            counts = Counter(binary)
            ans.append(counts['1'])
            
        return ans