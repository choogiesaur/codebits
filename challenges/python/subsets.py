# Generate all subsets of an array
# View it as:
# For any element, you can either use it in the subset or not
# This implementation isnt very fast on LC, research another
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def recurse(comb, i):
            if i == len(nums):
                result.append(comb)
                return
            
            recurse(comb, i+1)
            recurse(comb + [ nums[i] ], i+1)
            
        recurse([], 0)
        return result
