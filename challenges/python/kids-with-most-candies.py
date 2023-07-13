# LC 1431
# Observes what happens when you give any kid 'i' your extra candies, and output an
# array of True/False denoting whether or not kid[i] would have the most candies
# (More than one can have the most candies)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_encountered = 0
        for item in candies:
            max_encountered = max(max_encountered, item)

        ans = []
        for item in candies:
            if item + extraCandies >= max_encountered:
                ans.append(True)
            else:
                ans.append(False)

        return ans
