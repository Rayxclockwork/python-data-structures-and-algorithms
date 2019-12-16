class Node:
    def __init__(self, value):
        """creates new node when called"""
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        """creates new stack instance"""
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
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.value

    def peek(self):
        """returns value of top node"""
        if self.top != None:
            return self.top.value
        else:
            return None

    def is_empty(self):
        """returns boolean stating whether or not stack is empty"""
        if self.top == None:
            return True
        else:
            return False

class Queue:
    def __init__(self):
        """creates new instance of queue"""
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """adds new node to end of queue"""
        node = Node(value)
        node.next = self.rear
        self.rear = node
        if not self.front:
            self.front = node

    def dequeue(self):
        """removes node from beginning of queue"""
        if not self.front:
            raise EmptyQueueException('How Rude!')


        removed_node = self.front
        self.front = self.front.next
        removed_node.next = None
        return removed_node.value


    def peek(self):
        """returns value of node from beginning of queue"""
        if self.front != None:
            return self.front.value
        else:
            return None

    def is_empty(self):
        """returns boolean stating whether or not queue is empty"""
        if self.front == None:
            return True
        else:
            return False

class EmptyQueueException(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = ('Queue is Empty!')

