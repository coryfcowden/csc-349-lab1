# csc-349-lab1
singleton
A “divide and conquer” algorithm is one that divides a problem into smaller subproblems, solves those subproblems, and then combines the “sub-solutions” into a solution to the original problem.

Problem description:
A singleton is a single item, as opposed to two (or more) items grouped together, as in the “singleton pattern”, describing an object that may only be instantiated once, or a “singleton set”, a set containing only one element.
Consider the following problem: you are given a sorted sequence of integers. Within this sequence, one and only one element is unique; the other elements are all duplicated once.

For example:(−2,−2,5,5,12,12,67,67,72,80,80)

Implement a program in Python that reads a file containing such a sequence of integers (one per line) and returns that lone, unique, singleton element. In the example above, your algorithm should return 72.

Your program must accept as a command line argument the name of a file containing a sequence as described above, then print to stdout the singleton element.   I've uploaded an example Download example of such a file (the expected return is -64) and a simple test case generator Download test case generator.

You can assume the input will be valid (that is, a list with a nonzero number of elements, sorted in ascending order, with all but one element repeated twice), but you should guard about possible edge cases (for example, a list with 1 element, a list with the singleton element, a list where the singleton happens to be the first element you look at...)

Name your file studentID_lab1.py. Make sure your program prints nothing but the final answer to facilitate automatic grading. Usage example:

% python rcanaan_lab1.py unique-64

>>> -64
