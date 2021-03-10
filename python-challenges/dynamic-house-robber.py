# nums = [1,2,3,1]
nums = [2,7,9,3,1]

def rob(self, nums: List[int]) -> int:

	# Dict to keep track of max profit combo ending at i
	max_at_i = {}

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

	for i in range(len(nums) - 3):
		max_at_i[i + 3] = nums[i + 3] + max(max_at_i[i], max_at_i[i+1])

	# print(max_at_i[len(nums) - 1], max_at_i[len(nums) - 2])
	return max(max_at_i[len(nums) - 1], max_at_i[len(nums) - 2])

print(rob(nums))
