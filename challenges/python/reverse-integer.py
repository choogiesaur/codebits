# lc reverse integer
# given -1230, return -321
# given 1337 return 7331
# If outside 32 bit range -()
from collections import deque
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
            
        lst = deque()

        sign = -1 if x < 0 else 1

        x = abs(x)
        while x > 0:
            digit = x % 10
            lst.append(digit)
            x //= 10
        
        # fast forward zeroes
        while lst[0] == 0:
            lst.popleft()

        modifier = 1
        total = 0
        while lst:
            curr = lst.pop()
            total += curr * modifier
            modifier *= 10
        
        total *= sign

        if total < -(2**31) or total > (2**31) - 1:
            return 0
        
        return total
