# LC 392
# Passes most test cases
# Fails this s = abc, t = ahbgdc
# output: 
# match 0 0
# match 1 2
# match 2 5
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        t_ptr = 0

        if s == t:
            return True
        elif len(s) > len(t):
            return False

        found_on_current = False
        while s_ptr < len(s) and t_ptr < len(t):

            while t_ptr < len(t):
                if t[t_ptr] == s[s_ptr]:
                    print("match", s_ptr, t_ptr)
                    found_on_current = True
                    t_ptr += 1
                    break
                t_ptr += 1

            if t_ptr == len(t) and (found_on_current == False or s_ptr < len(s)):
                return False

            found_on_current = False
            s_ptr += 1
        
        return True
