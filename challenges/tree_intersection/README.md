# Challenge Summary
<!-- Short summary or background information -->
Traversing 2 binary trees, find all values that exist in both trees
Worked with Stephen Koch

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Our function goes through 2 binary trees recursively, adding all values to a hashtable. Every time a value already exists in a hashtable, that value gets added to a list.
The list of matching values is returned at the end.
Time and space are O(n) because the function needs to traverse the entirety of both trees, regardless of how large each tree is.

## Solution
<!-- Embedded whiteboard image -->
![whiteboard:](/assets/treeintersection.jpg)
