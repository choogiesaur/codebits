# remove dupes in place
# latest one....use two pointer tech!
# slow keeps track of the next unique element in the final sorted order
# fast explores the array to find the next unique element to swap into the slow pointers spot
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        slow = 0
        fast = 1
        while fast < len(nums):
            # nums are differnt, meaning we found a newly seen val
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1
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
                

## diff version that required returning k, number of unique elements
    ## find faster soln
    def removeDuplicates2(self, nums: List[int]) -> int:
        seen = set()
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                del nums[i]
            else:
                seen.add(nums[i])
                k += 1
                i += 1

        return k

        
