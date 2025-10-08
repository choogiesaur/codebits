from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)

        seen = set()

        for val in counts.values():
            if val in seen:
                return False
            else:    
                seen.add(val)
        return True
