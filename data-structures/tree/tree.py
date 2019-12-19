class _Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinaryTree():
	def __init__(self):
		self._root = None

	def pre_order(self, node=None, arr=[]):
		node = node or self._root
		arr.append(node.value)

		if node.left:
			self.pre_order(node.left, arr)

		if node.right:
			self.pre_order(node.right, arr)

		return arr

	def in_order(self,
		node=node or self._root

		if node.left:
			self.in_order

		arr.append(node.value)

		if node.right


class BinarySearchTree():
	def add(self, value):
		node = _Node(value)
		if not self._root:
			self._root = node
			return

		# what to do when there is a root?
		if value < self._root.value:
			# what
			if not self._root.left:
			self._root.left = node
		else:
			# what
			if not self._root.right:
self._root.right = node
