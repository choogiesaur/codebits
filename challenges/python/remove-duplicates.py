# remove dupes in place

# note on while/index:
# reevaluates len(nums) on each iteration 
# therefore deleting is safe as len will adjust
# on iteration, if it matches criteria, del and all items to the right push to left
# if not match criteria, increment index
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        members = set()
        i = 0
        while i < len(nums):
            if nums[i] in members:
                del nums[i]
            else:
                members.add(nums[i])
                i += 1
                
