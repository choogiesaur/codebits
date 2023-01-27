# Leetcode 724
# Keep running track of left sum (sum of all items to left of current index)
# Total sum of array is constant; Right sum can be gotten by subtracting current element from total sum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum = 0
        total_sum = sum(nums)

        for i in range(len(nums)):
            # print(i, left_sum, total_sum)
            total_sum -= nums[i]
            if left_sum == total_sum:
                return i
            left_sum += nums[i]


        return -1
