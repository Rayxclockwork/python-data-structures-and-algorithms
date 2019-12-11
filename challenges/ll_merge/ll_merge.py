class LinkedList:
	def __init__(self):
		"""starts empty linked list"""
		self.head = None

	def merge_lists(self, linked_list2):
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
