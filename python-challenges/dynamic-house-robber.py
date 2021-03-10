# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
nums = [2, 3, 1, 5, 7, 8, 4, 9]

# Problem: You have a row of houses to rob, with their monetary value expressed as a number.
# You want to maximize the profit you obtain without robbing any 2 houses that are adjacent to eachother.

# My algorithm:
# initialize m as such, where m[i] is the maximum profit possible for a combination of houses ending at i:
# m[0] = n[0]
# m[1] = max(n[0], n[1])
# m[2] = max(n[0] + n[2], n[1])
# after that...take the case of n[3]. to maximize profit:
# you can't add n[2], it is adjacent
# you could add n[1] and you could add n[0], so add the higher of the two
# if there was an element before that, i.e n[x]:
# n[X] n[0] n[1] n[2] n[3]
# then you could always add n[x] and n[x+2]; since elements are always >= 0, you can only increase profit
# so, iterate the array and at each index i: 
# max_at_i = arr[i] + max(max_at_i[i-2], max_at_i[i-3])

def rob(self, nums: List[int]) -> int:

	# Dict to keep track of max profit combo ending at i
	max_at_i = {}

	# Base cases
	if len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		return max(nums)
	if len(nums) == 3:
		return max(nums[0] + nums[2], nums[1])
	if len(nums) >= 4:
		max_at_i[0] = nums[0]
		max_at_i[1] = max(nums[0], nums[1])
		max_at_i[2] = max(nums[0] + nums[2], nums[1])
		
	# max at this location is this element plus larger of the maxes 2 spots and 3 spots ago
	for i in range(len(nums) - 3):
		max_at_i[i + 3] = nums[i + 3] + max(max_at_i[i], max_at_i[i+1])

	# Max possible for the entire array will either end at the last, or 2nd to last house
	return max(max_at_i[len(nums) - 1], max_at_i[len(nums) - 2])

print(rob(nums))

# VARIATION: Numbers can be negative!
# Solution: Any time you consider an element for addition to the subset, instead offer max(0, element)
# This way if it detracts value, dont add it
def maxSubsetSum(arr):
    max_at = {}
    total_max = 0
    
    length = len(arr)
    
    init1 = max(0, arr[0])
    init2 = max(0, max(arr[0], arr[1]))
    init3 = max(0, max(arr[1], max(0, arr[0]) + max(0,arr[2])))
    
    if length == 1:
        return init1
    elif length == 2:
        return init2
    elif length == 3:
        return init3
    
    max_at[0] = init1
    max_at[1] = init2
    max_at[2] = init3
    print("Base cases:", init1, init2, init3)
    for i in range(3, length):
        max_at[i] = max(max_at[i-2], max_at[i-3]) + max(0, arr[i])
        print(i, max_at[i])
        
    return max(max_at[length - 1], max_at[length - 2])

print(maxSubsetSum([3, 5, -7, 8, 10]))
