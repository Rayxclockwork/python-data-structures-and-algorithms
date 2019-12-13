class Node:
    def __init__(self, value):
        """creates new node when called"""
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        """creates new stack instance"""
        self.stack = []
        self.top = None

    def push(self):
        """pushes new node onto stack"""
        self.stack.append(0)

    def pop(self):
        """takes top node off stack"""
        self.stack.pop(0)

    def peek(self):
        """returns value of top node"""
        return self.top.value

    def is_empty(self):
        """returns boolean stating whether or not stack is empty"""
        if self.top == None:
            return True
        else:
            return False

class Queue:
    def __init__(self):
        """creates new instance of queue"""
        self.queue = []
        self.front = None

    def enqueue(self, value):
        """adds new node to end of queue"""
        current = self.front
        new_node = Node(value)
        if current is None:
            self.front = new_node
        else:
            while current.next:
                current = current.next
                current.next = new_node

    def dequeue(self):
        """removes node from beginning of queue"""
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        """returns value of node from beginning of queue"""
        return self.front.value

    def is_empty(self):
        """returns boolean stating whether or not queue is empty"""
        if self.front == None:
            return True
        else:
            return False
