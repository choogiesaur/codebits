### A Python implementation of a Stack data structure

class PyStack:

	# Internal class for items in stack
	class StackNode:
		def __init__(self, val = 0, child = None):
			self.val = val
			self.child = child

	# Check if stack has items
	def is_empty(self):
		return self.size() == 0

	# Get number of items in stack
	def get_size(self):
		return self.size

	# View topmost item without modifying stack
	def peek(self):
		if self.is_empty():
			print("Nothing left in stack.")
		else:
			return self.head.val

	# Remove topmost item and return its value (modifies stack)
	def pop(self):
		if self.is_empty():
			print("Nothing left in stack.")
		else:
			popped_val = self.head.val
			self.head = self.head.child
			self.size -= 1 
			return popped_val
		
	# Add item x to top of stack
	def push(self, x):

		# Temp node for what we are inserting
		new_node = self.StackNode(x, self.head)
		self.head = new_node
		self.size += 1
	
	# Constructor
	def __init__(self):
		self.head = None
		self.size = 0

### Testing code
my_stack = PyStack()
print(my_stack.get_size())

# Push 1
my_stack.push(1)
print(my_stack.get_size())
print(my_stack.peek())

# Push 4
my_stack.push(4)
print(my_stack.get_size())
print(my_stack.peek())

# Pop 4
my_stack.pop()
print(my_stack.peek())

# Pop 1
my_stack.pop()
print(my_stack.peek())
