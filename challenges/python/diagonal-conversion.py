class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        buckets = [[] for i in range(numRows)]

        i = 0
        direction = 1
        for c in s:
            # append curr char to curr row
            buckets[i].append(c)
            print(c)
            # can convert this to a single if with or for both conditions
            # and initialize to -1 so it hits 1 = 0 direction change 
            # in the if, *= to -1 regardless of which end we hit
            if i == numRows - 1:
                direction *= -1
            if i == 0:
                direction = 1
            i += direction
        
        # Now lets join the list
        # can prob make this more pythonic
        buckets = ["".join(x) for x in buckets]
        res = "".join(buckets)
        return res