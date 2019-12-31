from collections import deque

class _Node():
    def __init__(self, value):
        """Creates new node when called"""
        self.value = value
        self.left = None
        self.right = None
        self.next = None

class Queue:
    def __init__(self):
        """creates new instance of queue"""
        self.front = None

    def enqueue(self, value):
        """adds new node to end of queue"""
        new_node = _Node(value)
        if not self.front:
            self.front = new_node

        current = self.front
        while current.next:
            current = current.next
        current.next = new_node

    def dequeue(self):
        """removes node from beginning of queue"""
        if self.front == None:
            return ('Queue is empty')
        else:
            removed_node = self.front
            self.front = self.front.next
            return removed_node

    def peek(self):
        """returns value of node from beginning of queue"""
        if self.front:
            return self.front.value
        else:
            return None

    def is_empty(self):
        """returns boolean stating whether or not queue is empty"""
        if self.front == None:
            return True
        else:
            return False


class BinaryTree():
    def __init__(self):
        """Creates new instance of Binary Tree"""
        self._root = None

    def add(self, value):
        node = _Node(value)
        if not self._root:
            self._root = node
        q = Queue()

        q.enqueue(self._root.value)

        while not q.is_empty():
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left.value)
            else:
                current.left = node
                return
            if current.right:
                q.enqueue(current.right.value)
            else:
                current.right = node
                return


    def pre_order(self, node=None, arr=[]):
        """Starts at root, then moves left to right"""
        node = node or self._root

        if node is None:
            return []
        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)


        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def in_order(self, node=None, arr=[]):
        """Starts at left and moves over to root, then to the right"""
        node = node or self._root

        if node is None:
            return []

        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)

        return arr


    def post_order(self, node=None, arr=[]):
        """Starts at left, moves right, ends at root"""
        node = node or self._root

        if node is None:
            return []

        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr

    def find_maximum_value(self, node = None):
        node = node or self._root
        max = self._root.value

        if node is None:
            return None
        q = Queue()
        q.enqueue(self._root)

        while not q.is_empty():
            current = q.dequeue()
            if current.value > max:
                max = current.value
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)

            return max

    @staticmethod
    def breadth_first(tree, node=None, arr = None):
        """Starts at the root, moves to children left to right, then moves to those children left to right"""
        q = Queue()

        if arr is None:
            arr = []

        q.enqueue(tree._root)

        while not q.is_empty():
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            arr.append(current.value.value)

        return arr

class BinarySearchTree(BinaryTree):

    def add(self, value):
        """Adds node to a tree and places it dependent upon the rest of the tree"""
        node = _Node(value)
        if self._root is None:
            self._root = node
            return

        current = self._root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return
                else:
                    current = current.left

            else:
                if not current.right:
                    current.right = node
                    return
                else:
                    current = current.right

    def contains(self, value):
        """returns boolean that expresses whether or not value exists in binary tree"""
        if self._root == None:
            return False

        if self._root.value == value:
            return True

        current = self._root
        while True:
            if value == current.value:
                return True
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    return False

            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
