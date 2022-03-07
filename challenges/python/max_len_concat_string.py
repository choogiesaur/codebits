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
    
# Recursive soln...not that much faster
class Solution:
    global_result = 0
    def maxLength(self, arr: List[str]) -> int:
        # Array, starting index, starting string
        self.maxUnique(arr, 0, "")
        return self.global_result

    def num_unique_chars(self, s: str) -> bool:
        encountered = set()
        for char in s:
            if char in encountered:
                return -1
            encountered.add(char)
        return len(s)

    def maxUnique(self, arr, i, curr):
        if i == len(arr) and self.num_unique_chars(curr) > self.global_result:
            self.global_result = len(curr) # or result of num_unique_chars
            return
        if i == len(arr):
            return

        self.maxUnique(arr, i+1, curr)
        self.maxUnique(arr, i+1, curr + arr[i])
