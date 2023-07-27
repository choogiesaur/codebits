# LC 1137
class Solution:
    def tribonacci(self, n: int) -> int:
        d = {0: 0, 1: 1, 2: 1}

        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
            print(d[i])
        
        return d[n]
