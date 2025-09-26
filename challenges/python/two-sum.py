# lc1 :O
# given a target, return indices of two numbers that add up to target
# assume only one solution per list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[nums[i]] = i
