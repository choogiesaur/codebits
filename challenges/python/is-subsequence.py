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
