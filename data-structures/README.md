# linked_list

## Challenge
<!-- Description of the challenge -->
Practice traversing a linked list, inserting and moving nodes in a linked list

## API
<!-- Description of each method publicly available to your Linked List -->
includes - input is target value, output is true or false
insert - create a new node, and insert new node as head of linked list
append - creates a new node and tacks it to the end of the linked list
insert_before - takes in a value and a new value to be inserted, returns list with new node before the given value node
insert_after - same as before except it inserts the new node after the given value
kth_from_end - finds the value of the node at k from the end of the linked list

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Approach to append/insert before/and insert after was to loop through list to find the given value and create/insert a new node at that value; Big 0 for time is O(n) because, worst case, the given value is the end of the linked list. Big O of space is O(1) because its the same steps no matter what

Kth from end was to find the end of the list and insert node at end of list - k (sort of like relabeling the end of the list)
space - O(n) to find end of list

![whiteboard:](/assets/linkedlistchallenge.jpg)
![whiteboard:](/assets/kthfromend.jpg)
![whiteboard:](/assets/mergelists.jpg)
