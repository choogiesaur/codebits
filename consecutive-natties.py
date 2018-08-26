n = 9
count = 0
print "n = " + str(n)

for i in range(1,n):
	total = 0
	lst = []
	for j in range(i,n):
		total = total + j
		lst.append(j)
		if total == n:
			count = count + 1
			print lst
			break
		elif total > n:
			break

print "There are " + str(count) + " sequences of consecutive natural numbers with a sum of " + str(n)