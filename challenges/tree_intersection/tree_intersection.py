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
        self.dq = deque()
    def enqueue(self, value):
        self.dq.appendleft(value)
    def dequeue(self):
        return self.dq.pop()
    def is_empty(self):
        return len(self.dq) == 0


class BinaryTree():
    def __init__(self):
        """Creates new instance of Binary Tree"""
        self._root = None

    def add(self, value):
        node = _Node(value)
        if not self._root:
            self._root = node
            return

        q = Queue()
        q.enqueue(self._root)

        while not q.is_empty():
            current = q.dequeue()
            if not current.left:
                current.left = node
                return
            if not current.right:
                current.right = node
                return
            q.enqueue(current.left)
            q.enqueue(current.right)



def tree_intersection(tree_1, tree_2):
    ht = set()
    lst = []
	
    def recurse_traverse(node):
        if not node:
            return

        recurse_traverse(node.left)
        recurse_traverse(node.right)
        if node.value in ht:

            lst.append(node.value)
        ht.add(node.value)
    
    recurse_traverse(tree_1._root)
    recurse_traverse(tree_2._root)
    return lst



if __name__ == '__main__':
	tree_1 = BinaryTree()
	tree_1.add(12)
	tree_1.add(18)
	tree_1.add(5)
	tree_1.add(22)
	tree_1.add(6)

	tree_2 = BinaryTree()
	tree_2.add(8)
	tree_2.add(12)
	tree_2.add(5)
	tree_2.add(21)
	tree_2.add(4)

	tree_intersection(tree_1, tree_2)