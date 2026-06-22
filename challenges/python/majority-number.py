# lc 169
# return element that appears more than (n / 2) times
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        highest = -1
        dct = defaultdict(int)
        half = len(nums) / 2
        
        for num in nums:
            dct[num] += 1
            highest = max(highest, dct[num])
            if highest > half:
                return num