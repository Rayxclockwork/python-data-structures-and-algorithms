# Hashmap Left Join

## Challenge
<!-- Description of the challenge -->
Write a function to left-join 2 hashtables

Worked with Sharmarke

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
This function loops over the keys in a hashtable and looks for the same value in a second hashtable.

If the key exists in the second hashtable, the value at that key is added to the output.

If the key is not in the second hashtable, None is added to the output instead.

Big O of space and time is O(n) as the tables are not a pre-determined size and the function needs to loop through the entirety of both tables

## Solution
<!-- Embedded whiteboard image -->
![whiteboard:](/assets/leftjoin.jpg)
