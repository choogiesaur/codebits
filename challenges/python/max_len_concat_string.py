import itertools

# Determines if input string contains only unique characters or not
def contains_unique(s: str) -> bool:
    encountered = set()
    for char in s:
        if char in encountered:
            return False
        encountered.add(char)
    return True
  
# Use itertools to generate all combinations of list, check each for uniqueness, return length of largest one
# Kinda slow! Recursive soln better
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_length = 0
        for L in range(0, len(arr)+1):
            for subset in itertools.combinations(arr, L):
                concatenated = ''.join(subset)
                if contains_unique(concatenated):
                    print(concatenated)
                    max_length = max(max_length, len(concatenated))
        return max_length
