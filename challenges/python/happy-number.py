# LC 202
class Solution:
    def isHappy(self, n: int) -> bool:
        encountered = set()

        while n not in encountered:

            encountered.add(n)

            curr_sum = 0
            while n > 0:
                curr_sum += (n % 10) ** 2
                n = n // 10
            n = curr_sum

            if n == 1:
                return True

        return False
