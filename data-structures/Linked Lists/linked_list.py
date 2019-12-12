# import pdb


class Node:
    """creates new node when called"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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

    def insert(self, value):
        """Instantiates new node as head"""
        current = self.head
        new_node = Node(value, current)
        self.head = new_node

    def __str__(self):
        """returns stringified contents of linked list"""
        return str(LinkedList)

    def append(self, value):
        """appends new node to the end of list"""
        current = self.head
        new_node = Node(value)
        if current is None:
            self.head = new_node
        else:
            while current.next:
                current = current.next
                current.next = new_node

    def insert_after(self, value, new_value):
        """inserts new node after given target value"""
        new_node = Node(new_value)
        current = self.head
        while current.value != value:
            current = current.next
            new_node.next = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
        """inserts new node before a given target value"""
        current = self.head
        new_node = Node(new_value)
        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def kth_from_end(self, k):
        """finds value of node that's kth from end of list"""
        current = self.head
        length = 0
        try:
            while current.next:
                current = current.next
                length += 1

            while length - k < length:
                current = self.head
                current = current.next
                print('line 82', current.next.value)
                return current.next.value
        except Exception as e:
            print('#84 current', e)


ll = LinkedList()
ll.insert(1)
ll.insert(12)
ll.insert(3)
ll.insert(5)
ll.insert(7)
ll.insert(11)
ll.insert(51)
print('#95 current', ll.kth_from_end(5))
