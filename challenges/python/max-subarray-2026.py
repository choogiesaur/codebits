# most pythonic yet
# passing case of [-1] required picking initial curr,max correctly
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -(10**4)
        
        for item in nums:
            curr_sum = max(curr_sum + item, item)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
            