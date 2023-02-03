# LC 409

from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # character counts, f for found characters without repeats
        d = defaultdict(int)
        f = set()

        for char in s:
            d[char] += 1
            f.add(char)
        
        if len(f) == 1:
            return len(s)

        total_len = 0
        found_singleton = False
        for char in f:
            # add all to length, they are pairable
            if d[char] % 2 == 0:
                total_len += d[char]
            # we have a char that was only found once
            else:
                if d[char] > 1: # case where a letter has pairs, but one left over. ex: 'ccc' has 3 occurrences of c, we need to count all the pairs
                    total_len += d[char] - 1
                found_singleton = True
        
        # can only insert a singleton in one place, once: the middle
        if found_singleton:
            total_len += 1

        return total_len
