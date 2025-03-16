# Q1

## Q1.1

### Implementation

Max Heapify was implemented using both iterative and recursive methods. Each method was used to implement a Build Max Heap. The Verify Max Heap function was used to verify the resulting arrays.

### Results

The iterative and recursive Build Max Heaps were succesfully able to max heapify an array. As expected, the recursive method took longer than the iterative. This is probably due to the overhead created for each recursive call.

Initially, the recursive method was taking longer than the iterative. The was because the recusive method's array2 was being shallow copied from the iterative method's array1. Due to the recursive method being called after the iterative, array2 was already sorted when the recursive method was called, leading to an O(n) runtime.

## Q1.2

**Plateau Valley Sort:**

Assumptions:

1. Sort will run in O(n) time.
2. Even indices will be Valleys.
3. Odd indices will be Plateaus.
4. Iterate from index = 1 (second value) to the end of the array.

Steps:

1. If index is odd

   1. Check if the value to the left (index - 1) is larger.
   2. If it is larger, swap. If not, do nothing.
2. If index is even

   1. Check if the value to the left is less.
   2. If it is less, swap. If not, do nothing.


# Q2.1, Q2.2, Q3.1

Submitted via pdf


# Q3.2

## a

### Implementation

Quicksort and an Optimzied Bubble Sort were implemented. The Bubble Sort was optimized by adding a swap flag. If
