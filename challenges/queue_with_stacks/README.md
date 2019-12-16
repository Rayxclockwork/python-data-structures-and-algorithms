# Challenge Summary
<!-- Short summary or background information -->
Using 2 stacks, use a PsuedoQueue class to make the stacks act like a queue(enqueue/dequeue instead of push/pop)

## Challenge Description
<!-- Description of the challenge -->
The challenge is getting stacks to react the same way as a queue without actually instantiating a new queue class

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Given a stack, use push/pop to move information into another stack that will allow the stacks to work with Queue methods:
-Given a stack of [5]->[10]->[15]->[20], you can dequeue 20 by flipping the positions of each stack item

## Solution
<!-- Embedded whiteboard image -->
![whiteboard:](/assets/psuedoqueue.jpg)