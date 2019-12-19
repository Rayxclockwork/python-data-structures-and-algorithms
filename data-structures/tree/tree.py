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

    def pre_order(self, node=None, arr=[]):
        """Starts at root, then moves left to right"""
        node = node or self._root
        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)


        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def in_order(self, node=None, arr=[]):
        """Starts at left and moves over to root, then to the right"""
        node=node or self._root

        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.left, arr)

        return arr


    def post_order(self, node=None, arr=[]):
        """Starts at left, moves right, ends at root"""
        node=node or self._root

        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr


class BinarySearchTree(BinaryTree):

    def add(self, value):
        """Adds node to a tree and places it dependent upon the rest of the tree"""
        node = _Node(value)
        if not self._root:
            self._root = node
            return

        if value < self._root.value:
            if not self._root.left:
            self._root.left = node

        else:
			if not self._root.right:
            self._root.right = node


    def contains(self, value):
        """returns boolean that expresses whether or not value exists in binary tree"""
        if self._root.value == value:
            return True

        elif:
            if root.right == None:
                return False
            else:
                return BinarySearchTree.contains(self._root.right, value)
        else:
            if root.left == None:
                return False
            else:
                return BinarySearchTree.contains(self._root.left, value)
