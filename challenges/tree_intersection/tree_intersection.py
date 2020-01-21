class Hashtable:
    def __init__(self, length=4):
        self.array = [None] * length

    def hashing(self, key):
        length = len(self.array)
        return hash(key) % length

    def get(self, key):
        i = self.hashing(key)
        print(self.array)
        if self.array[i] is None:
            raise KeyError()
        else:
            for key_value_pair in self.array[i]:
                if key_value_pair[0] == key:
                    return key_value_pair[1]

            raise KeyError()


    def contains(self, key):
        i = self.hashing(key)
        if self.array[i] is None:
            return False
        else:
            for key_value_pair in self.array[i]:
                if key_value_pair[0] == key:
                    return True
            return False

    def add(self, key, value):
        i = self.hashing(key)
        if self.array[i] is not None:
            for key_value_pair in self.array[i]:
                if key_value_pair[0] == key:
                    key_value_pair = value
                    break
            else:
                self.array[i].append([key, value])
        else:
            self.array[i] = []
            self.array[i].append([key, value])

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

        else:
            current = self._root
            q = Queue()
            q.enqueue(current)
            while not q.is_empty():
                current = q.dequeue()
                if not current.left:
                    current.left = node
                    return
                else:
                    q.enqueue(current.left)
                if not current.right:
                    current.right = node
                    return
                else:
                    q.enqueue(current.right)


def recurse_traverse(node, ht, lst):
	if not node:
		return
	recurse_traverse(node.left, ht, lst)
	recurse_traverse(node.right, ht, lst)
	if ht.contains(node.value):
		lst.append(node.value)
	ht.add(node.value, node.value)


def tree_intersection(tree_1, tree_2):
	ht = Hashtable()
	lst = []
	
	recurse_traverse(tree_1._root, ht, lst)
	recurse_traverse(tree_2._root, ht, lst)
	print(lst)
	return lst

	

if __name__ == '__main__':
	tree_1 = BinaryTree()
	tree_1.add(12)
	tree_1.add(18)
	tree_1.add(5)
	tree_1.add(22)
	tree_1.add(6)

	tree_2 = BinaryTree()
	tree_2.add(12)
	tree_2.add(8)
	tree_2.add(5)
	tree_2.add(21)
	tree_2.add(4)

tree_intersection(tree_1, tree_2)