test_string = "(([])){}{}[]"
# test_string = "(([]))"

def isValid(s: str) -> bool:
	# Python EZ-Stack:
	# Just use List with append(), pop() // both run in O(1) time

	stackerooni = []

	for char in s:
		if char == '(' or char == '{' or char == '[':
			stackerooni.append(char)
			print("Appended", char)
		elif char == ')' and stackerooni[-1] == '(' or \
			 char == '}' and stackerooni[-1] == '{' or \
			 char == ']' and stackerooni[-1] == '[':
			print("Popping", stackerooni.pop())
		else:
			return False
	return True

print(isValid(test_string))
