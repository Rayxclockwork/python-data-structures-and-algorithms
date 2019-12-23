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
	
	def fizz_buzz_tree(self, node=None, arr=[]):
		node = node or self._root

		if node is None:
			return []

		current = self._root
		while True:
			if current.node.value % 15 == 0:
				current.node.value = 'FizzBuzz'

			if current.node.value % 3 == 0:
				current.node.value = 'Fizz'

			if current.node.value % 5 == 0:
				current.node.value = 'Buzz'


	## % 15, then 3, then 5 == 0
	## loop, then modify values in given tree
	## reassign value of node to fizz, buzz, or FizzBuzz