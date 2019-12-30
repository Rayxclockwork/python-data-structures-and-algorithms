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
        current = self.front
        new_node = _Node(value)
        if current is None:
            self.front = new_node
        else:
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
            return removed_node.value

    def peek(self):
        """returns value of node from beginning of queue"""
        if self.front:
            return self.front.value
        else:
            return None



class BinaryTree():
    def __init__(self):
        """Creates new instance of Binary Tree"""
        self._root = None


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

    def breadth_first(self, node=None):
        """Starts at the root, moves to children left to right, then moves to those children left to right"""
        q = []

        if self._root:
            q.append(self._root.value)
        else:
            return None


        while (len(q) > 0):
            node = q.pop(0)

            if node.left is not None:
                q.append(node.left.value)

            if node.right is not None:
                q.append(node.right.value)

        return q

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
