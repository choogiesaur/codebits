class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # midpoint odd: n // 2 (exact)
        # midpoint evn: n // 2 (use < to not touch it)
        str_x = str(x)
        if len(str_x) % 2 == 0:
            even = True
        else:
            even = False

        if len(str_x) == 1:
            return True

        mid = len(str_x) // 2

        for i in range(mid):
            opp = -(i+1)
            if str_x[i] != str_x[opp]:
                return False
        
        return True