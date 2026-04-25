# lc intersection of 2 arrays II
# find intersection of the two arrays,
# each element in the intersection should appear as many times as 
# it overlaps in both arrays
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a_counts = Counter(nums1)
        b_counts = Counter(nums2)
        
        x_counts = Counter()
        
        for k,v in a_counts.items():
            x_counts[k] = min(a_counts[k], b_counts[k])
            
        # elements is an iterable. represents each item as many times as the counts
        # cast it to a list to get a list with as many occurrences as there are 
        # in the counter
        return list(x_counts.elements())