# lc
# every input array has exactly 1 number that appears once
# find and return it, in linear time with constant extra space
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        
        for num in nums:
            dct[num] += 1
            
        for k, v in dct.items():
            if v == 1:
                return k
        