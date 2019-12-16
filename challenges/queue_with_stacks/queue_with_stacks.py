class Node:
	def __init__(self, value):
		"""creates new node when called"""
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	def push(self, value):
		"""pushes new node onto stack"""
		new_node = Node(value)
		if self.top is None:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node

	def pop(self):
		"""takes top node off stack"""
		if self.top == None:
			return
		else:
			popped_node = self.top
			self.top = self.top.next
		return popped_node.value

	def peek(self):
		"""returns value of top node"""
		if self.top != None:
			return self.top.value
		else:
			return

class PseudoQueue:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
    def enqueue(self, value):
        self.stack_one.push(value)
        if self.stack_one.top.next == None:
            self.front = self.stack_one.top
    def dequeue(self):
        while self.stack_one.top:
            node = self.stack_one.pop()
            self.stack_two.push(node)
        queue_front = self.stack_two.pop()
        self.front = self.stack_two.top
        while self.stack_two.top:
            node = self.stack_two.pop()
            self.stack_one.push(node)
        return queue_front
