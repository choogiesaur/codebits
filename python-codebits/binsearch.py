# iterative implementation of binary search
def binsearch_iterative(lst, x):
	left 	= 0
	right 	= len(lst) - 1

	while right >= left:
		mid 	= left + (right - left) / 2
		print "left: ", left, " mid: ", mid, " right: ", right

		if lst[mid] == x:
			print x, " found at: ", mid
			return
		elif x < lst[mid]:
			right = mid - 1
		elif x > lst[mid]:
			left = mid + 1

	print x, "not found"

lol = [1,2,3,4,5,6,7,8,9,10]
binsearch_iterative(lol, 1)

# recursive implementation
def binsearch_recursive(lst, left, right, x):
	if right >= left:
		mid = left + (right - left) / 2
		print "left: ", left, " mid: ", mid, " right: ", right

		if lst[mid] == x:
			print x, "found at: ", mid
			return
		elif x < lst[mid]:
			return binsearch_recursive(lst, left, mid-1, x)
		elif x > lst[mid]:
			return binsearch_recursive(lst, mid+1, right, x)
	
	print x, "not found"

lmao = [1,2,3,4,5]
binsearch_recursive(lmao, 0, len(lmao)-1, 4)
