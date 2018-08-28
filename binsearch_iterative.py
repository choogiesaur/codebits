def binsearch(lst, x):
	left 	= 0
	right 	= len(lst) - 1
	mid 	= left + (right - left) / 2
	# can just put this in beginning of while loop

	while right >= left:
		print "left: ", left, " mid: ", mid, " right: ", right

		if lst[mid] == x:
			print x, " found at: ", mid
			return
		elif x < lst[mid]:
			right = mid - 1
		elif x > lst[mid]:
			left = mid + 1

		mid = left + (right - left) / 2

	print x, "not found"

lol = [1,2,3,4,5,6,7,8,9,10]
binSearch(lol, 9)
