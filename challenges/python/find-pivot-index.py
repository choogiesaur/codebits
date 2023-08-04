# LC 724
# Keep running track of left sum (sum of all items to left of current index)
# Total sum of array is constant; Right sum can be gotten by subtracting current element from total sum
class Solution:
    
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)

        for i in range(len(nums)):
            total_sum -= nums[i]
            if left_sum == total_sum:
                return i
            left_sum += nums[i]
            
        return -1
        
    # Diff solution, less big brain tbh
    def pivotIndex(self, nums: List[int]) -> int:
        left_sums = []
        rite_sums = []

        curr_sum = 0
        for item in nums:
            left_sums.append(curr_sum)
            curr_sum += item
        
        curr_sum = 0
        for i in range(len(nums)):
            rite_sums.append(curr_sum)
            curr_sum += nums[-(i+1)]

        for i in range(len(nums)):
            left = left_sums[i]
            rite = rite_sums[-(i+1)]
            if left == rite:
                return i
        
        return -1
