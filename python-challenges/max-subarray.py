nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray(self, nums: List[int]) -> int:
	# can use (-sys.maxint) - 1
	curr_max = -(10 ** 5) - 1 # 1 less than min nums[i]

	# Key: index, Val: Max sum for a subarray ending at this point
	d = {}

	for i in range(len(nums)):
		# Base case: 1st element
		if i == 0:
			# Largest sum ending at index 0 is whatever is at index zero
			d[i]     = nums[i]
			curr_max = nums[i]
		else:
			# The max subarray ending at this index is either: the current element, or
			# The max subarray ending at previous index *plus* the current element
			max_at_i = max(nums[i], d[i-1] + nums[i])
			curr_max = max_at_i if max_at_i > curr_max else curr_max

			# memo-ize the max subarray for current index
			d[i] = max_at_i

	return curr_max

print(max_subarray(nums))
