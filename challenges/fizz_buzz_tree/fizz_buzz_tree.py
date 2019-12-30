class _Node():
    def __init__(self, value):
        """Creates new node when called"""
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
	def __init__(self):
		"""Creates new instance of Binary Tree"""
		self._root = None
	
	
def fizz_buzz_tree(tree):
	# node = _Node or tree._root

	# if node is None:
	# 	return []

	# current = tree._root
	# while True:
	# 	if current.node.value % 15 == 0:
	# 		current.node.value = 'FizzBuzz'

	# 	if current.node.value % 3 == 0:
	# 		current.node.value = 'Fizz'

	# 	if current.node.value % 5 == 0:
	# 		current.node.value = 'Buzz'

	def fizzify(num):
		adjusted_val = None

		if num % 15 == 0:
			adjusted_val = 'FizzBuzz'

		if num % 3 == 0:
			adjusted_val = 'Fizz'

		if num % 5 == 0:
			adjusted_val = 'Buzz'

		if adjusted_val == None:
			return str(num)
		else:
			return adjusted_val
	
	def traverse(root):
		if not root:
			return None

		fizzified = fizzify(root.value)

		new_node = _Node(fizzified)

		new_node.left = traverse(root.left)

		new_node.right = traverse(root.right)

		return new_node
	
	
	fizzy_tree = BinaryTree()

	fizzy_tree._root = traverse(tree)

	return fizzy_tree

	## % 15, then 3, then 5 == 0
	## loop, then modify values in given tree
	## reassign value of node to fizz, buzz, or FizzBuzz