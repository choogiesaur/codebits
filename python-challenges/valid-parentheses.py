test_string = "(([])){}{}[]"
# test_string = "(([]))"

def isValid(self, s: str) -> bool:
	# Python EZ-Stack:
	# Just use List with append(), pop() // both run in O(1) time

	stackerooni = []

	for char in s:
		# If opening character, push it onto stack
		if char == '(' or char == '{' or char == '[':
			stackerooni.append(char)

		# If closing character but there's nothing on the stack, invalid
		elif (char == ']' or char == '}' or char == ')') and len(stackerooni) == 0:
			return False

		# If closing character and matching opening char is ontop of stack, proceed
		elif char == ')' and stackerooni[-1] == '(' or \
			 char == '}' and stackerooni[-1] == '{' or \
			 char == ']' and stackerooni[-1] == '[':
			stackerooni.pop()
		else:
			return False

	# If youve gotten through all characters and nothing left in stack, string is valid!    
	if len(stackerooni) == 0:
		return True
	else:
		return False

print(isValid(test_string))
