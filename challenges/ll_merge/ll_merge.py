class LinkedList:
    def __init__(self):
        """starts empty linked list"""
        self.head = None

        def merge_lists(self, ll2):
         ll1_current = self.head
         ll2_current = ll2.head

          while ll1_current != None and ll2_current != None:
          	ll1_next = ll1_current.next
            ll2_next = ll2_current.next

            ll2_current.next = ll1_next
            ll1_current.next = ll2_current

            ll1_next = ll1_current
            ll2_next = ll2_current

            ll2_current = ll2.head
            return self
