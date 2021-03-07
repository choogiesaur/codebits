class PythonStackerooni:

	# Internal class for stack items
	class StackNode:
		def __init__(self, val, child):
			self.val = val
			self.child = child

	def is_empty(self):
		return self.size() == 0

	def get_size(self):
		return self.size

	def peek(self):
		if self.get_size() == 0:
			print("Nothing left in stack.")
		else:
			return self.head.val

	# Push item x onto stack
	def push(self, x):

		# Temp node for what we are inserting
		new_node = self.StackNode(x, self.head)
		self.head = new_node
		self.size += 1


	def pop(self):
		temp = self.head.val
		if self.get_size() == 0:
			print("Nothing left in stack.")
		else:
			self.head = self.head.child
			self.size -= 1 
			return temp

	def __init__(self):
		self.head = None
		self.size = 0

my_stack = PythonStackerooni()
print(my_stack.get_size())

my_stack.push(1)
print(my_stack.get_size())
print(my_stack.peek())

my_stack.push(4)
print(my_stack.peek())

my_stack.pop()
print(my_stack.peek())

my_stack.pop()
print(my_stack.peek())