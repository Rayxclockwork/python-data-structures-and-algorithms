class LinkedList:
	def __init__(self):
		"""starts empty linked list"""
		self.head = None

	def insert(self, value):
        """Instantiates new node as head"""
        current = self.head
        new_node = Node(value, current)
        self.head = new_node


	def merge_lists(self, linked_list1, linked_list2):
		"""zip-merges 2 linked lists together"""
		linked_list1_current = self.head
		linked_list2_current = linked_list2.head

		while linked_list1_current != None and linked_list2_current != None:
			linked_list1_next = linked_list1_current.next
			linked_list2_next = linked_list2_current.next

			linked_list2_current.next = linked_list1_next
			linked_list1_current.next = linked_list2_current

			linked_list1_next = linked_list1_current
			linked_list2_next = linked_list2_current

		linked_list2_current = linked_list2.head
		return self


linked_list1 = LinkedList()
linked_list1.insert(1)
linked_list1.insert(12)
linked_list1.insert(3)
linked_list1.insert(5)
linked_list1.insert(7)
linked_list1.insert(11)
linked_list1.insert(51)



linked_list2 = LinkedList()
linked_list2.insert(18)
linked_list2.insert(4)
linked_list2.insert(9)
linked_list2.insert(2)
linked_list2.insert(6)
linked_list2.insert(13)
linked_list2.insert(45)