# Q1) Merging *k **sorted* lists into one sorted list (25 points)**

## Psuedocode

In order to merge k sorted lists into one sorted list:

- Initialize new empty sorted list, "sorted"
- Place smallest element of each k sorted lists into a min-heap
- Move top element (smallest) of min-heap to "sorted"
- Replace the element moved to "sorted" with the next value from the k sorted list it was taken from
- Repeat this for each n elements

## Asymptotic Analysis

This meets **O(n log k)** because:

- Inserting an element into a min-heap with height of log k is O(log k)
- Taking the top element from min-heap is O(1)
- A new element is inserted and popped for each of n elements, so total time is O( n(log k + 1) ), which is O(n log k)

## Implementation

### Split 1,000,000 integers into 100 groups of 10,000 integers

- Divide original[ 0 : 999,999 ] into sub-lists so that: sub_list_1[ 0 : 9999 ] ... sub_list_100[ 990,000 : 999,999 ] are generated.

### Sort 50 groups with Radix + Counting Sort

- Sort 50 of the sublists using Radix Sort, with counting sort as the underlying sort for each digit.
- Results in 50 of the 100 sorted sub-lists to merge.

### Sort 50 groups with Bucket sort

- Sort 50 of the sublists uing Bucket sort.
- Results in 50 of the 100 sorted sub-lists to merge.

### Merge 100 groups

- Merge the 100 sorted sub-lists into one sorted list, "sorted", using the algorithm described in the Psuedocode section.

## Discussion: O(n log k) vs O(n k)
