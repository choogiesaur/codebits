# Find all contiguous subarrays whose sum == k
# Works but n^2...and times out
def subarraySum(self, nums: List[int], k: int) -> int:

	if len(nums) == 1:
		return 1 if nums[0] == k else 0

	num_subarrays = 0

	# Dictionary to keep track of subarray sums
	d = {}
	d[(0, 0)] = nums[0] # Initialize first subarray sum

	# Prestore sums of "simple" subarrays: [0:x]
	for i in range(1, len(nums)):
		curr_sum  = d[(0, i-1)] + nums[i]
		d[(0, i)] = curr_sum

	for i in range(len(nums)):
		for j in range(i, len(nums)):
			if i == j:
				curr_sum = nums[i]
			elif i == 0:
				curr_sum = d[(0, j)]
			else:
				curr_sum = d[(0, j)] - d[(0, i-1)]
			# print(str(i) + ', ' + str(j) + ':', curr_sum)
			if curr_sum == k:
				num_subarrays += 1                

	return num_subarrays
