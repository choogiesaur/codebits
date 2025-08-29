# lc334
# in list, find indices i,j,k such that
# a[i] < a[j] < a[k]
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = c = (2**31)-1
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            elif num <= c:
                return True

        return False
