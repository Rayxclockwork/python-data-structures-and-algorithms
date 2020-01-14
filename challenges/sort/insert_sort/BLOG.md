#### So you have to sort a list.
*Without* a built in function.

Luckily I'm here to help.
First let's look at the list - 

+ [10, 3, 15, 8, 20]

Doesn't seem hard for our brains to process that.\
Unfortunately for us, our brains are trained to do things like this.\
Computers aren't.

1. So to sort this list in code, look at the first index -
+ 10

2. Then our next number:

+ 3

3. 3 is less than 10 so three is 'kept out' while the rest of the list is looped through.

When our loop sees 3 as the smallest, we will get 3 and 10 switched, giving us:

+ [3, 10, 15, 8, 20]

Steps 1, 2, and 3 will repeat for each index of the list until we get back:

+ [3, 8, 10, 15, 20]


There are plenty of good pseudocode examples out there if you're still lost.

Go forth and conquer!

###### (Sorting lists at least)
