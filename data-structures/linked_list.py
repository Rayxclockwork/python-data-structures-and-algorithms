class LinkedList:
    def __init__(self):
        """starts empty linked list"""
        self.head = None

    def includes(self, target):
        """searches linked list to find specific value"""
        current = self.head
        while current:
            if current.value == target:
                return True
        current = current.next
        return False

    def insert(self, data):
        """Instantiates new node as head"""
        new_node = Node(data)
        self.head = new_node

    def __str__(self):
        if self.size > 1:
            return str(LinkedList)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            self.head = self.head.ref
            self.head.ref = new_node

    def insert_after(self, value, new_value):
        while current.next:
            if 

    def insert_before(self, value, new_value):
        current = self.head
        while current.next:
            if current.next.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node


class Node(LinkedList):

    def __init__(self, value):
        self.value = value
        self.next = None
