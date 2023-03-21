# another solution that was just as fast
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j = 0
        for char in s:
            found_curr = False
            if j == len(t):
                return False
            
            while j < len(t):
                if char == t[j]:
                    found_curr = True
                    j += 1
                    break
                j += 1

            if not found_curr:
                return False
        return True

# LC 392

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0

        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        while i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

            if i == len(s):
                return True
            elif j == len(t) and i < len(s):
                return False
