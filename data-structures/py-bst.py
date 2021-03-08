class BinarySearchTree:
	
	# Internal class for nodes in tree
	class TreeNode:
		def __init__(self, val = 0, left = None, right = None):
			self.val 	= val
			self.left 	= left
			self.right 	= right

		def has_left_child(self):
			return self.left != None

		def has_right_child(self):
			return self.right != None
	
	# Constructor for BST
	def __init__(self, root = None):
		self.root = root
		# node_array = []

	# O(logn) insertion into BST
	# Solidify: Handle duplicates?
	def insert(self, x):

		if self.root == None:
			self.root = self.TreeNode(x)
			return
		
		prev = self.root
		curr = self.root

		while(curr):
			prev = curr
			if x <= curr.val:
				curr = curr.left
			else:
				curr = curr.right

		if x <= prev.val:
			prev.left = self.TreeNode(x)
		else:
			prev.right = self.TreeNode(x)

	# Insert without keeping track of prev
	# Checks if node has child before moving downward
	def insert_2(self, x):

		if self.root == None:
			self.root = self.TreeNode(x)
			return

		curr = self.root
		new_node = self.TreeNode(x)

		while(curr):
			if x <= curr.val:
				if curr.has_left_child():
					curr = curr.left
				else:
					curr.left = new_node
					return
			else:
				if curr.has_right_child():
					curr = curr.right
				else:
					curr.right = new_node
					return

	# Preorder traversal; Default uses tree's root
	def preorder(self, curr_node):
		if curr_node == None:
			return

		# Root, Left, Right
		print(curr_node.val)
		self.preorder(curr_node.left)
		self.preorder(curr_node.right)

	def inorder(self, curr_node):
		if curr_node == None:
			return

		# Left, Root, Right
		self.inorder(curr_node.left)
		print(curr_node.val)
		self.inorder(curr_node.right)

	def postorder(self, curr_node):
		if curr_node == None:
			return

		# Left, Right, Root
		self.postorder(curr_node.left)
		self.postorder(curr_node.right)
		print(curr_node.val)


	def dfs(self, node, mode):
		if mode == 'inorder':
			return self.inorder(node)
		elif mode == 'preorder':
			return self.preorder(node)
		elif mode == 'postorder':
			return self.postoder(node)

"""
Testing area
"""

bst = BinarySearchTree()

bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(7)

root = bst.root

print("Preorder traversal:")
bst.preorder(root)

print("Inorder traversal:")
bst.inorder(root)

print("Postorder traversal:")
bst.postorder(root)


mode = "inorder"
print("Initiate DFS using mode: ", mode)
bst.dfs(root, mode)