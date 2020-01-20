# Challenge Summary
<!-- Short summary or background information -->
Without using a built in method, find the first repeated word in a string

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Each word of the string is looped over and added to a set
If the word is in the set, it is returned as the answer, otherwise it is added to the set until a repeated word is found or the end of the string.
Big O time is O(n) as, worst case, it could loop through the whole string with no repeated words

## Solution
<!-- Embedded whiteboard image -->
![whiteboard:](/assets/wordrepeat.jpg)