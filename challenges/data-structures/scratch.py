
    def __init__(self, data, next):
        """starts empty linked list"""
        self.data = data
        self.next = None
        self.head = None

    def includes(self, target):
        """searches linked list to find specific value"""
        if not self.head:
            return False

        current = self.head
        while current:
            if current.value == target:
                return True
        current = current.next
        return False

    def insert(self, item):
        """Instantiates new node as head"""
       new_node = Node(data, self.head)
       self.head = newNode
       self.size+=1

    def __str__():
        if self.size > 1:
            return

# No public methods
# 2 attributes/properties - next, value
class Node:
    pass

    def __init__(self, value):
        self.value = value
        self.next = None
