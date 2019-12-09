class LinkedList:
    def __init__(self, data, next):
        """starts empty linked list"""
        self.data = data
        self.next = None
        self.head = None

    def includes(self, target):
        """searches linked list to find specific value"""
        # if not self.head:
        #     return False

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
        self.size += 1

    def __str__(self):
        if self.size > 1:
            return str(LinkedList)


class Node(LinkedList):

    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('5')
node5 = Node('12')
node6 = Node('4')
node7 = Node('15')
